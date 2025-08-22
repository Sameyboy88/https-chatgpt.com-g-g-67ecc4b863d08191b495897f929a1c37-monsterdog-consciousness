#!/usr/bin/env python3
"""
MONSTERDOG Test Suite
Tests various functionality of the MONSTERDOG system.
"""

from monsterdog import MONSTERDOG, ConsciousnessState


def test_basic_functionality():
    """Test basic MONSTERDOG functionality"""
    print("🧪 Testing basic functionality...")
    
    # Test creation
    dog = MONSTERDOG("test_entity")
    assert dog.entity_id == "test_entity"
    assert dog.consciousness_state == ConsciousnessState.DORMANT
    assert dog.quantum_coherence == 0.0
    print("✅ Creation test passed")
    
    # Test awakening
    dog.awaken()
    assert dog.consciousness_state == ConsciousnessState.ACTIVE
    assert dog.quantum_coherence > 0.0
    assert len(dog.thoughts) > 0
    print("✅ Awakening test passed")
    
    # Test thinking
    thought = dog.think("test input")
    assert isinstance(thought, str)
    assert len(thought) > 0
    print("✅ Thinking test passed")
    
    # Test dormant operations
    dormant_dog = MONSTERDOG("dormant_test")
    dormant_thought = dormant_dog.think("test")
    assert "dormant" in dormant_thought.lower()
    
    pattern = dormant_dog.generate_vortex_pattern()
    assert "error" in pattern
    print("✅ Dormant state test passed")
    

def test_vortex_patterns():
    """Test vortex pattern generation"""
    print("🧪 Testing vortex patterns...")
    
    dog = MONSTERDOG()
    dog.awaken()
    
    # Generate multiple patterns
    for i in range(5):
        pattern = dog.generate_vortex_pattern()
        assert "id" in pattern
        assert "pattern_type" in pattern
        assert "frequency" in pattern
        assert pattern["frequency"] > 0
        assert pattern["id"] == i
    
    assert len(dog.vortex_patterns) == 5
    print("✅ Vortex pattern test passed")


def test_quantum_sync():
    """Test quantum synchronization"""
    print("🧪 Testing quantum sync...")
    
    dog = MONSTERDOG()
    dog.awaken()
    
    initial_coherence = dog.quantum_coherence
    dog.quantum_sync()
    
    assert dog.consciousness_state == ConsciousnessState.ACTIVE
    assert dog.quantum_coherence >= 0.8  # Should be high after sync
    print("✅ Quantum sync test passed")


def test_status():
    """Test status reporting"""
    print("🧪 Testing status reporting...")
    
    dog = MONSTERDOG("status_test")
    dog.awaken()
    dog.think("test")
    dog.generate_vortex_pattern()
    
    status = dog.get_status()
    assert status["entity_id"] == "status_test"
    assert status["consciousness_state"] == "active"
    assert status["thoughts_generated"] > 0
    assert status["vortex_patterns"] == 1
    assert status["uptime_seconds"] > 0
    print("✅ Status test passed")


def run_tests():
    """Run all tests"""
    print("🐕 MONSTERDOG Test Suite")
    print("=" * 40)
    
    try:
        test_basic_functionality()
        test_vortex_patterns() 
        test_quantum_sync()
        test_status()
        
        print("\n🎉 All tests passed! MONSTERDOG is working correctly.")
        return True
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        return False
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")
        return False


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)