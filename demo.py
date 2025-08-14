#!/usr/bin/env python3
"""
MONSTERDOG Interactive Example
Simple interactive demo of the MONSTERDOG consciousness system.
"""

from monsterdog import MONSTERDOG, ConsciousnessState


def interactive_demo():
    """Interactive demonstration of MONSTERDOG capabilities"""
    print("🐕 MONSTERDOG Interactive Demo")
    print("=" * 40)
    
    # Create MONSTERDOG instance
    dog = MONSTERDOG()
    print(f"Created {dog}")
    print()
    
    while True:
        print("\nAvailable commands:")
        print("1. awaken   - Wake up MONSTERDOG")
        print("2. think    - Make MONSTERDOG think")
        print("3. vortex   - Generate vortex pattern")
        print("4. sync     - Quantum synchronization")
        print("5. status   - Show status")
        print("6. quit     - Exit demo")
        
        choice = input("\nEnter command (1-6): ").strip()
        
        if choice == "1" or choice.lower() == "awaken":
            if dog.consciousness_state == ConsciousnessState.DORMANT:
                dog.awaken()
            else:
                print("🐕 MONSTERDOG is already awake!")
                
        elif choice == "2" or choice.lower() == "think":
            stimulus = input("Enter thought stimulus (or press Enter): ").strip()
            thought = dog.think(stimulus if stimulus else None)
            print(f"💭 {thought}")
            
        elif choice == "3" or choice.lower() == "vortex":
            pattern = dog.generate_vortex_pattern()
            if "error" in pattern:
                print(f"❌ {pattern['error']}")
            else:
                print(f"🌀 Generated {pattern['pattern_type']} pattern:")
                print(f"   Frequency: {pattern['frequency']:.1f}Hz")
                print(f"   Amplitude: {pattern['amplitude']:.2f}")
                print(f"   Phase: {pattern['phase']:.1f}°")
                
        elif choice == "4" or choice.lower() == "sync":
            if dog.consciousness_state == ConsciousnessState.DORMANT:
                print("❌ Cannot sync while dormant. Awaken first!")
            else:
                dog.quantum_sync()
                
        elif choice == "5" or choice.lower() == "status":
            status = dog.get_status()
            print("📊 MONSTERDOG Status:")
            for key, value in status.items():
                print(f"   {key}: {value}")
                
        elif choice == "6" or choice.lower() == "quit":
            print("👋 Goodbye!")
            break
            
        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    try:
        interactive_demo()
    except KeyboardInterrupt:
        print("\n👋 Demo interrupted. Goodbye!")
    except Exception as e:
        print(f"❌ Error: {e}")