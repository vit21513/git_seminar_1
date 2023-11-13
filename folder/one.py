def start(foo):
    
    if isinstance(foo,(int,float)):
        return f"its number {foo*12}" 
    return f"its string {foo}!!!"



if __name__== "__main__":
    print(start(5.2))
    print(start("5.2"))   