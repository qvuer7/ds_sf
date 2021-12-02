import numpy as np 

def game() -> int:
    """Let user guess random number

    Returns:
        int: number of attempts user take to guess
    """
    number = np.random.randint(1,100)
    count = 0
    
    while True: 
        count +=1 
        predicted = int(input('give me your guess ->'))
        
        if predicted > number : 
            print("predicted is more then actual")
        elif predicted < number: 
            print("predicted is less then actual")
        else: 
            break
        
    return count

if __name__ == "__main__":
    print(f'You gessed the number in {game()} attempts')

    