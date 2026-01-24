import sys

def main():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    operations = input_data[1:]
    
    volume = 0
    is_playing = False 
    
    for op in operations:
        op_code = int(op)
        
        if op_code == 1:
            volume += 1
            
        elif op_code == 2:
            if volume > 0:
                volume -= 1
                
        elif op_code == 3:
            is_playing = not is_playing
            
        if volume >= 3 and is_playing:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()
