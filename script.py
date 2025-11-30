# Number Guessing
import random

def number_guess():
    """Generate a random number between 1 and 100"""
    return random.randint(1, 100)

def play_game():
    """Play one round of the guessing game"""
    print('$' * 35)
    print("\nWelcome To The Number Guessing Game\n")
    print("$" * 35)
    print("🎯 I'm thinking of a number between 1-100")
    print("🎲 You have 7 attempts to guess it!\n")
    
    # Generate secret number ONCE
    correct_num = number_guess()
    attempts_left = 7
    
    while attempts_left > 0:
        try:
            user_guess = int(input(f"Attempt {8 - attempts_left}/7 - Your guess: "))
            
            # Validate range
            if user_guess < 1 or user_guess > 100:
                print("❌ Out of range! Please guess between 1-100\n")
                continue
            
            # Check guess
            if user_guess > correct_num:
                print("📉 Too high!")
                attempts_left -= 1
                if attempts_left > 0:
                    print(f"💡 {attempts_left} attempts left\n")
                    
            elif user_guess < correct_num:
                print("📈 Too low!")
                attempts_left -= 1
                if attempts_left > 0:
                    print(f"💡 {attempts_left} attempts left\n")
                    
            else:
                print(f"\n🎉 CONGRATULATIONS! You guessed it!")
                print(f"✅ The number was {correct_num}")
                print(f"🏆 You won in {8 - attempts_left} attempts!\n")
                return True  # Won!
                
        except ValueError:
            print("❌ Please enter a valid number!\n")
    
    # If loop ends, they lost
    print(f"\n💀 Game Over! You ran out of attempts!")
    print(f"🔢 The number was {correct_num}\n")
    return False  # Lost

def main():
    """Main game loop with replay option"""
    while True:
        play_game()
        
        # Ask to play again
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            print("\n👋 Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
