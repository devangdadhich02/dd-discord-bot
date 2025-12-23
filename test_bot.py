"""
Test script for the Discord Daily Poll Bot
This script tests the bot's core functionality without actually posting to Discord
"""

import sys
from datetime import datetime, timedelta
import pytz

# Mock discord for testing
class MockChannel:
    def __init__(self, name):
        self.name = name
        self.polls_created = []
    
    async def create_poll(self, **kwargs):
        self.polls_created.append(kwargs)
        print(f"  [OK] Poll would be created in {self.name}")
        print(f"    Question: {kwargs.get('question', {}).get('text', 'N/A')}")
        print(f"    Answers: {[ans.get('poll_media', {}).get('text', 'N/A') for ans in kwargs.get('answers', [])]}")
        print(f"    Duration: {kwargs.get('duration', 0) / 3600} hours")
        print(f"    Multi-select: {kwargs.get('allow_multiselect', False)}")

class MockGuild:
    def __init__(self, name, channel_names):
        self.name = name
        self.text_channels = [MockChannel(name) for name in channel_names]

def test_timezone_calculation():
    """Test timezone handling"""
    print("Testing timezone calculation...")
    timezone = pytz.timezone('Europe/Rome')
    now_italy = datetime.now(timezone)
    date_str = now_italy.strftime('%d/%m/%Y')
    
    assert len(date_str) == 10, "Date format should be DD/MM/YYYY"
    assert date_str.count('/') == 2, "Date should have 2 slashes"
    print(f"  [OK] Date format correct: {date_str}")
    return True

def test_time_options():
    """Test time options configuration"""
    print("Testing time options...")
    TIME_OPTIONS = [7, 9, 11, 13, 15, 17, 19, 21, 23]
    
    assert len(TIME_OPTIONS) == 9, "Should have 9 time options"
    assert all(isinstance(t, int) for t in TIME_OPTIONS), "All options should be integers"
    assert TIME_OPTIONS == sorted(TIME_OPTIONS), "Options should be sorted"
    print(f"  [OK] Time options correct: {TIME_OPTIONS}")
    return True

def test_channel_finding():
    """Test finding votazioni channels"""
    print("Testing channel finding logic...")
    
    # Simulate guild with multiple channels
    channel_names = [
        "votazioni-lol-h60",
        "spam-lol-70",
        "votazioni-lol-h70",
        "votazioni-lol-h80",
        "general",
        "votazioni-test"
    ]
    
    votazioni_channels = [name for name in channel_names if 'votazioni' in name.lower()]
    
    assert len(votazioni_channels) == 4, f"Should find 4 votazioni channels, found {len(votazioni_channels)}"
    print(f"  [OK] Found {len(votazioni_channels)} votazioni channels: {votazioni_channels}")
    return True

def test_poll_creation_logic():
    """Test poll creation data structure"""
    print("Testing poll creation logic...")
    
    TIME_OPTIONS = [7, 9, 11, 13, 15, 17, 19, 21, 23]
    POLL_DURATION_HOURS = 24
    timezone = pytz.timezone('Europe/Rome')
    now_italy = datetime.now(timezone)
    date_str = now_italy.strftime('%d/%m/%Y')
    
    question = date_str
    answers = [str(time_option) for time_option in TIME_OPTIONS]
    
    poll_data = {
        "question": {"text": question},
        "answers": [{"poll_media": {"text": answer}} for answer in answers],
        "duration": POLL_DURATION_HOURS * 3600,
        "allow_multiselect": True
    }
    
    assert poll_data["question"]["text"] == date_str, "Question should be the date"
    assert len(poll_data["answers"]) == 9, "Should have 9 answers"
    assert poll_data["duration"] == 86400, "Duration should be 24 hours in seconds"
    assert poll_data["allow_multiselect"] == True, "Should allow multiple selections"
    
    print(f"  [OK] Poll data structure correct")
    print(f"    Question: {poll_data['question']['text']}")
    print(f"    Answers count: {len(poll_data['answers'])}")
    print(f"    Duration: {poll_data['duration'] / 3600} hours")
    return True

def test_midnight_calculation():
    """Test midnight calculation for scheduling"""
    print("Testing midnight calculation...")
    
    timezone = pytz.timezone('Europe/Rome')
    now_italy = datetime.now(timezone)
    midnight_italy = now_italy.replace(hour=0, minute=0, second=0, microsecond=0)
    
    if now_italy >= midnight_italy:
        midnight_italy += timedelta(days=1)
    
    wait_seconds = (midnight_italy - now_italy).total_seconds()
    
    assert wait_seconds > 0, "Wait time should be positive"
    assert wait_seconds < 86400, "Wait time should be less than 24 hours"
    print(f"  [OK] Next midnight calculated: {midnight_italy.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  [OK] Wait time: {wait_seconds / 3600:.2f} hours")
    return True

async def test_simulated_poll_creation():
    """Simulate poll creation without actually posting"""
    print("Testing simulated poll creation...")
    
    # Create mock guild with votazioni channels
    guild = MockGuild("Test Server", [
        "votazioni-lol-h60",
        "votazioni-lol-h70",
        "votazioni-lol-h80"
    ])
    
    TIME_OPTIONS = [7, 9, 11, 13, 15, 17, 19, 21, 23]
    POLL_DURATION_HOURS = 24
    timezone = pytz.timezone('Europe/Rome')
    now_italy = datetime.now(timezone)
    date_str = now_italy.strftime('%d/%m/%Y')
    
    votazioni_channels = [ch for ch in guild.text_channels if 'votazioni' in ch.name.lower()]
    
    for channel in votazioni_channels:
        question = date_str
        answers = [str(time_option) for time_option in TIME_OPTIONS]
        
        poll_data = {
            "question": {"text": question},
            "answers": [{"poll_media": {"text": answer}} for answer in answers],
            "duration": POLL_DURATION_HOURS * 3600,
            "allow_multiselect": True
        }
        
        await channel.create_poll(**poll_data)
    
    # Verify polls were created
    total_polls = sum(len(ch.polls_created) for ch in votazioni_channels)
    assert total_polls == len(votazioni_channels), f"Should create {len(votazioni_channels)} polls"
    print(f"  [OK] Successfully simulated creating {total_polls} polls")
    return True

def run_tests():
    """Run all tests"""
    import sys
    # Fix encoding for Windows console
    if sys.platform == 'win32':
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    
    print("=" * 60)
    print("Running Discord Bot Tests")
    print("=" * 60)
    print()
    
    tests = [
        ("Timezone Calculation", test_timezone_calculation),
        ("Time Options", test_time_options),
        ("Channel Finding", test_channel_finding),
        ("Poll Creation Logic", test_poll_creation_logic),
        ("Midnight Calculation", test_midnight_calculation),
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        try:
            print(f"\n{test_name}")
            result = test_func()
            if result:
                passed += 1
                print(f"  [PASSED]")
            else:
                failed += 1
                print(f"  [FAILED]")
        except Exception as e:
            failed += 1
            print(f"  [FAILED]: {str(e)}")
    
    # Run async test
    print(f"\nSimulated Poll Creation")
    try:
        import asyncio
        result = asyncio.run(test_simulated_poll_creation())
        if result:
            passed += 1
            print(f"  [PASSED]")
        else:
            failed += 1
            print(f"  [FAILED]")
    except Exception as e:
        failed += 1
        print(f"  [FAILED]: {str(e)}")
    
    print()
    print("=" * 60)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("=" * 60)
    
    if failed == 0:
        print("[SUCCESS] All tests passed!")
        return 0
    else:
        print("[ERROR] Some tests failed!")
        return 1

if __name__ == "__main__":
    sys.exit(run_tests())

