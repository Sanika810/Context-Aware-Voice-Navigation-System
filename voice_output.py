from speak import speak, shutdown_speaker

class VoiceOutput:
    def __init__(self):
        pass
    
    def generate_voice_instruction(self, instruction, detections, current_speed):
        """Generate highly detailed and contextual voice instructions"""
        
        action = instruction['action']
        urgency = instruction['urgency']
        
        # Get nearby objects for context
        nearby_objects = [d for d in detections if d['distance'] < 40]
        critical_objects = [d for d in detections if d.get('urgency_score', 0) > 70]
        
        # EMERGENCY STOP SCENARIOS with turn options
        if action == 'EMERGENCY_STOP':
            if instruction.get('immediate_threats'):
                threat = instruction['immediate_threats'][0]
                threat_type = threat['class']
                threat_distance = threat['distance']
                
                # Check turn availability
                left_clear = '✓' in instruction['turn_opportunities'].get('left', '')
                right_clear = '✓' in instruction['turn_opportunities'].get('right', '')
                
                if left_clear and right_clear:
                    return f"EMERGENCY STOP! {threat_type} at {threat_distance:.0f} meters. Both left and right turns are available for evasion."
                elif left_clear:
                    return f"EMERGENCY STOP! {threat_type} at {threat_distance:.0f} meters. Left turn available for evasion. Right side blocked."
                elif right_clear:
                    return f"EMERGENCY STOP! {threat_type} at {threat_distance:.0f} meters. Right turn available for evasion. Left side blocked."
                else:
                    return f"CRITICAL! {threat_type} at {threat_distance:.0f} meters. Both sides blocked. Stop immediately and assess situation."
        
        # ... [Include all voice generation logic from original code]
        
        # FALLBACK: Use the primary instruction
        primary_text = instruction['primary_instruction']
        clean_text = primary_text.replace('⚠️', '').replace('🛑', '').replace('➡️', '').strip()
        return clean_text
    
    def speak_instruction(self, instruction, detections, current_speed):
        """Generate and speak instruction"""
        message = self.generate_voice_instruction(instruction, detections, current_speed)
        speak(message)
    
    def shutdown(self):
        """Cleanup voice system"""
        shutdown_speaker()
