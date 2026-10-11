# speak.py - GUARANTEED SOFT VOICE with Google TTS
import pygame
import threading
import tempfile
import os
import time
from gtts import gTTS
import queue

print("🎵 LOADING GOOGLE TTS - NATURAL VOICE...")

# Global variables
_speak_queue = queue.Queue(maxsize=3)
_is_speaking = False
_shutdown = False

def _google_tts_worker():
    """Worker thread using Google's natural TTS voices"""
    global _is_speaking
    
    pygame.mixer.init()
    
    print("✅ Google TTS Voice System Ready!")
    
    while not _shutdown:
        try:
            text = _speak_queue.get(timeout=0.5)
            
            if text is None:  # Shutdown signal
                break
                
            if not text.strip():
                continue
                
            _is_speaking = True
            
            try:
                # Create temporary file
                with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmpfile:
                    # Generate speech with Google's natural voice
                    tts = gTTS(
                        text=text,
                        lang='en',
                        slow=False,  # Normal speed = softer
                        lang_check=False
                    )
                    tts.save(tmpfile.name)
                    
                    # Play the audio
                    pygame.mixer.music.load(tmpfile.name)
                    pygame.mixer.music.play()
                    
                    # Wait for playback to complete
                    while pygame.mixer.music.get_busy() and not _shutdown:
                        time.sleep(0.1)
                    
                    # Clean up
                    os.unlink(tmpfile.name)
                    
            except Exception as e:
                print(f"🎵 TTS Error: {e}")
                
            _is_speaking = False
            
        except queue.Empty:
            continue
            
    pygame.mixer.quit()

# Start the worker thread
_tts_thread = threading.Thread(target=_google_tts_worker, daemon=True)
_tts_thread.start()

def speak(text):
    """Speak text using Google's natural voice"""
    global _is_speaking
    
    if not text or not isinstance(text, str):
        return
        
    text = text.strip()
    if not text:
        return
    
    # Soften the text for more pleasant speech
    soft_text = _soften_speech_text(text)
    print(f"🎵 {soft_text}")
    
    if _is_speaking:
        return  # Skip if already speaking
        
    try:
        _speak_queue.put_nowait(soft_text)
    except queue.Full:
        pass  # Skip if queue is full

def _soften_speech_text(text):
    """Convert text to softer, more natural speech patterns"""
    # Replace harsh commands with polite ones
    replacements = {
        'EMERGENCY STOP': 'Please stop immediately',
        'CRITICAL': 'Important',
        'STOP': 'Please stop',
        'SLOW DOWN': 'Please slow down', 
        'REDUCE SPEED': 'Please reduce speed',
        'YIELD': 'Please yield',
        '!': '.'
    }
    
    for harsh, soft in replacements.items():
        text = text.replace(harsh, soft)
    
    return text

def stop_speech():
    """Stop any currently playing speech"""
    pygame.mixer.music.stop()

def shutdown_speaker():
    """Shutdown the TTS system"""
    global _shutdown
    _shutdown = True
    stop_speech()
    try:
        _speak_queue.put_nowait(None)
    except:
        pass

print("✅ Google TTS System Loaded Successfully!")
