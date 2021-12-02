import numpy as np


def predict_number(number:int, min:int, max:int) -> int:
    """computer guess random number

    Args:
        number (int): number to guess
        min (int): lower border of randomisation
        max (int): highest border of randomisation

    Returns:
        int: number of attempts taken
    """
    
    count = 0 

    while True:
        
        count+=1
        predicted = np.random.randint(min,max)
        
        if predicted > number: 
            max = predicted
        elif predicted < number: 
                min = predicted
        else: 
            break
        
    return count

def mean_attempts(predict_number) -> int: 
    """calculate avarage number of steps taken to guess random number

    Args:
        predict_number ([type]): prediction function

    Returns:
        int: avarage number of guesses
    """
    
    s = 0
    
    for _ in range(1,100):
        
        number = np.random.randint(1,100)
        s += predict_number(number, 1,100)
        
    return s/100

if __name__ == '__main__':
    print(f'Avrage number of steps taken for laptop to guess the number = {mean_attempts(predict_number)}')