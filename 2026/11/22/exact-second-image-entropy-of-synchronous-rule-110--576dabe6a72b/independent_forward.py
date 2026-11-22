"""Independent literal two-pass Rule-110 output enumeration (Python standard library).

Directly enumerates initial windows; does not use graph, bitmask transitions,
subset minimization, matrix powers, or an entropy approximation.
"""

def Boolean110(left,center,right):
    return int((not center and right) or (center and not(left and right)))

def outputs(t,n):
    distinct=set()
    for state in range(1<<(n+2*t)):
        width=n+2*t
        tape=[(state>>(width-1-i))&1 for i in range(width)]
        for _ in range(t):
            tape=[Boolean110(tape[j],tape[j+1],tape[j+2])
                  for j in range(len(tape)-2)]
        assert len(tape)==n
        distinct.add(tuple(tape))
    return len(distinct)

if __name__=='__main__':
    target_t1=[1,2,4,8,16,31,59,112,213,405,769,1459,2768]
    target_t2=[1,2,4,8,16,31,59,112,213,405,768,1451,2732]
    for t,expected in ((1,target_t1),(2,target_t2)):
        for n in range(1,13):
            found=outputs(t,n)
            assert found==expected[n],(t,n,found,expected[n])
        print('time',t,': independent two-pass exact enumeration n=1..12 passed')
    print('VERIFY_INDEPENDENT_OK')
