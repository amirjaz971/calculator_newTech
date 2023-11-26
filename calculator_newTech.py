import math
off=True

    
while off:
        
    
        press_button=input('ON/OFF:')
        if press_button.upper()=='OFF':
            print('The calculator is already off!')
        elif press_button.upper()=='ON':
            on=True
        
            while on:
               try: 
                expression=input('Enter the expression: ') #The example for expression input---->3+5*4/2-8+math.sqrt(4)+abs(-4)+2**4+pow(2,3)
            
            
                if expression.upper()=='ON':
                    
                    print('The calculator is already ON!')
                elif expression.upper()=='OFF':
                    on=False
                    off=False
                    print('exiting.....')
                    break 
                else:
                    print(f'{expression}={eval(expression)}')
               except NameError:
                   print('Invalid format!')  
                             
        else:
            print('Wrong command!')        

          