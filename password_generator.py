#!/usr/bin/env python3
"""
🔐 Password Generator
Generate secure random passwords
"""
import random
import string
import argparse

def generate_password(length=16, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    """Generate a secure random password"""
    chars = ""
    if use_lower:
        chars += string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation
    
    if not chars:
        chars = string.ascii_letters + string.digits
    
    return ''.join(random.choice(chars) for _ in range(length))

def generate_passphrase(word_count=4, separator="-"):
    """Generate a memorable passphrase"""
    words = [
        "cyber", "shield", "vault", "cipher", "secure", "defend", "protect",
        "guard", "fortress", "binary", "firewall", "token", "encrypt", "decode",
        "quantum", "neural", "vector", "matrix", "shadow", "stealth", "phantom",
        "dragon", "phoenix", "titan", "apollo", "nova", "cosmic", "pixel",
        "crypto", "hidden", "secret", "mystic", "wizard", "knight", "guardian"
    ]
    return separator.join(random.choice(words) for _ in range(word_count))

def main():
    parser = argparse.ArgumentParser(description="Generate secure passwords")
    parser.add_argument("-l", "--length", type=int, default=16, help="Password length")
    parser.add_argument("-n", "--count", type=int, default=5, help="Number of passwords")
    parser.add_argument("--no-upper", action="store_true", help="Exclude uppercase")
    parser.add_argument("--no-digit", action="store_true", help="Exclude digits")
    parser.add_argument("--no-special", action="store_true", help="Exclude special chars")
    parser.add_argument("--passphrase", action="store_true", help="Generate passphrase instead")
    
    args = parser.parse_args()
    
    print("\n🔐 Password Generator")
    print("=" * 40)
    
    if args.passphrase:
        print(f"\n📝 Passphrase ({args.count}):")
        for i in range(args.count):
            print(f"  {i+1}. {generate_passphrase(args.length if args.length > 4 else 4)}")
    else:
        print(f"\n🔑 Random Passwords (length: {args.length}):")
        for i in range(args.count):
            password = generate_password(
                length=args.length,
                use_upper=not args.no_upper,
                use_digits=not args.no_digit,
                use_special=not args.no_special
            )
            print(f"  {i+1}. {password}")

if __name__ == "__main__":
    main()
