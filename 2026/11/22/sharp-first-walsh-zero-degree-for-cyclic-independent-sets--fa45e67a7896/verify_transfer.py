"""Independent 2x2 transfer and free-product syllable checks.
Run with Python 3 standard library. Tests only finite ranges.
"""

def product_trace(n,mask):
    a,b,c,d=1,0,0,1
    for i in range(n):
        s= -1 if mask>>i & 1 else 1
        a,b,c,d=a+b,s*a,c+d,s*c
    return a+d

def normal_form(n,mask):
    # T and R are independent free-product factors of orders 2 and 3.
    st=[]
    def push(x,v=1):
        if st and st[-1][0]==x:
            old=st.pop()[1]; val=(old+v)%(2 if x=='T' else 3)
            if val:st.append((x,val))
        else:st.append((x,v))
    for i in range(n):
        if (mask>>i)&1==0:push('T')
        push('R')
    while len(st)>1 and st[0][0]==st[-1][0]:
        x,v=st.pop(0);push(x,v)
    return st

if __name__=='__main__':
    for n in range(3,16):
        z=0; min_w=n+1
        for mask in range(1<<n):
            tr=product_trace(n,mask)
            normal=normal_form(n,mask)
            assert (tr==0)==(normal==[('T',1)]),(n,mask,tr,normal)
            if tr==0:
                z+=1; min_w=min(min_w,mask.bit_count())
        assert (z==0 if n%3 else min_w==n//3+1)
        print('GROUP',n,z, None if z==0 else min_w)
    # Matrix identities direct.
    def mul(A,B):
        a,b,c,d=A;e,f,g,h=B
        return (a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h)
    plus=(1,1,1,0);minus=(1,-1,1,0);ident=(1,0,0,1)
    def word(chars):
        x=ident
        for ch in chars:x=mul(x,plus if ch=='+' else minus)
        return x
    assert word('---')==(-1,0,0,-1)
    assert word('+--+')==tuple(-v for v in minus)
    print('IDENTITIES PASS')
