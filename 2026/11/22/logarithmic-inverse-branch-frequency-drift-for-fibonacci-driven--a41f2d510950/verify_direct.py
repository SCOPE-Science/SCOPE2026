"""Independent direct recurrence check through Fibonacci substitution depth 32."""
def main():
    w0,w1='0','1'
    expected={0:[3,-1,-1,-1],16:[0,-4,20,-16],32:[9,5,17,-31]}
    for n in range(33):
        if n in expected:
            ds=[]
            for s in range(4):
                a,b=s>>1,s&1
                num=0
                for c in w0:
                    num+=(a==0 and b==0)
                    a,b=b,a^b^int(c)
                ds.append(4*num-len(w0))
            assert ds==expected[n],(n,ds)
            print('PASS direct word depth',n,'length',len(w0),'D',ds)
        if n<32:w0,w1=w0+w1,w0
if __name__=='__main__':main()
