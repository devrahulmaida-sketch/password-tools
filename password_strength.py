#!/usr/bin/env python3
"""
🔍 Password Strength Checker
Analyze password strength and provide suggestions
"""
import string
import math

COMMON_PASSWORDS = [
    "password", "123456", "12345678", "qwerty", "abc123", "monkey", "1234567",
    "letmein", "trustno1", "dragon", "baseball", "iloveyou", "master", "sunshine",
    "ashley", "bailey", "passw0rd", "shadow", "123123", "654321", "superman"
]

def check_strength(password):
    """Check password strength and return score"""
    score = 0
    feedback = []
    
    # Length checks
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")
    
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1
    
    # Character checks
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    if has_lower:
        score += 1
    else:
        feedback.append("Add lowercase letters")
    
    if has_upper:
        score += 1
    else:
        feedback.append("Add UPPERCASE letters")
    
    if has_digit:
        score += 1
    else:
        feedback.append("Add numbers (0-9)")
    
    if has_special:
        score += 1
    else:
        feedback.append("Add special characters (!@#$%)")
    
    # Common password check
    if password.lower() in COMMON_PASSWORDS:
        score = 1
        feedback = ["This is a commonly used password!"]
    
    # Sequential characters check
    if has_sequential(password):
        score -= 1
        feedback.append("Avoid sequential characters (abc, 123)")
    
    # Repeated characters check
    if has_repeated(password):
        score -= 1
        feedback.append("Avoid repeated characters (aaa, 111)")
    
    # Calculate entropy
    entropy = calculate_entropy(password)
    
    # Strength label
    if score <= 2:
        strength = "❌ Very Weak"
    elif score <= 4:
        strength = "⚠️ Weak"
    elif score <= 6:
        strength = "✅ Fair"
    elif score <= 8:
        strength = "✅✅ Strong"
    else:
        strength = "🛡️🛡️🛡️ Very Strong"
    
    return {
        "score": max(0, score),
        "strength": strength,
        "entropy": entropy,
        "feedback": feedback
    }

def has_sequential(password):
    """Check for sequential characters"""
    for i in range(len(password) - 2):
        if ord(password[i+1]) == ord(password[i]) + 1 and ord(password[i+2]) == ord(password[i]) + 2:
            return True
    return False

def has_repeated(password):
    """Check for repeated characters"""
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            return True
    return False

def calculate_entropy(password):
    """Calculate password entropy in bits"""
    if not password:
        return 0
    
    charset_size = 0
    if any(c.islower() for c in password):
        charset_size += 26
    if any(c.isupper() for c in password):
        charset_size += 26
    if any(c.isdigit() for c in password):
        charset_size += 10
    if any(c in string.punctuation for c in password):
        charset_size += 32
    
    if charset_size == 0:
        return 0
    
    entropy = len(password) * math.log2(charset_size)
    return round(entropy, 2)

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Check password strength")
    parser.add_argument("-p", "--password", type=str, help="Password to check")
    args = parser.parse_args()
    
    if not args.password:
        password = input("\n🔍 Enter password to check: ")
    else:
        password = args.password
    
    result = check_strength(password)
    
    print(f"\n📊 Password Strength Analysis")
    print("=" * 40)
    print(f"Strength: {result['strength']}")
    print(f"Score: {result['score']}/10")
    print(f"Entropy: {result['entropy']} bits")
    
    if result['feedback']:
        print(f"\n💡 Suggestions:")
        for fb in result['feedback']:
            print(f"  • {fb}")

if __name__ == "__main__":
    main()
