#!/usr/bin/env python3
"""Independent bit-array enumeration on three-row Life cylinders; standard library."""

def evolve(mask,n):
    cells=[(mask>>k)&1 for k in range(3*n)]
    answer=0
    for x in range(n):
        for y in range(3):
            count=0
            for dx in (-1,0,1):
                for dy in (-1,0,1):
                    if dx==dy==0:continue
                    yy=y+dy
                    if 0<=yy<3:count+=cells[3*((x+dx)%n)+yy]
            old=cells[3*x+y]
            if count==3 or (count==2 and old):answer|=1<<(3*x+y)
    return answer

def main():
    expected={3:(26,26),4:(14,22),5:(102,112),6:(314,338)}
    checked=0
    for n,(want_f,want_t) in expected.items():
        fixed=return2=0
        for mask in range(1<<(3*n)):
            y=evolve(mask,n)
            fixed+=(y==mask)
            return2+=(evolve(y,n)==mask)
            checked+=1
        assert (fixed,return2)==(want_f,want_t),(n,fixed,return2)
        print(f'independent n={n}: fixed={fixed}, two_return={return2}, primitive_two={(return2-fixed)//2}')
    print(f'independent states tested={checked}; PASS')
if __name__=='__main__':main()
