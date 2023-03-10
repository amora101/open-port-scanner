from scanner.scanner import normal_scan
import timeit

def hello():
    print("Hello, world!")

if __name__ == '__main__':
    # normal_scan(target = '18.196.110.53')
    # normal_scan(target = '18.196.110.53')
    # timeit.timeit('normal_scan(target = "18.196.110.53")')    
    t = timeit.timeit(hello, number=1)/10
    print(f"{t:.6f}")