from math import comb, factorial

def multinomial(m,a,b,c):
    return factorial(m)//(factorial(a)*factorial(b)*factorial(c))

def check(m):
    total_fixed=total_orbits=osc_basin=last_layer=0
    basin_profile={2**c:0 for c in range(1,m+1)}
    for a in range(m+1):
        for b in range(m-a+1):
            c=m-a-b
            multiplicity=multinomial(m,a,b,c)
            total_fixed += multiplicity*(m+c+2)
            total_orbits += multiplicity*c
            osc_basin += multiplicity*c*2**c
            if c:
                last_layer += multiplicity*(a+b)*2**c
                basin_profile[2**c] += multiplicity*c
    assert total_fixed==2*(2*m+3)*3**(m-1)
    assert total_orbits==m*3**(m-1)
    assert osc_basin==2*m*4**(m-1)
    assert last_layer==m*(2*4**(m-1)-2**m)
    for c in range(1,m+1):
        assert basin_profile[2**c]==comb(m,c)*2**(m-c)*c
    total_states=2*(m+1)*4**m
    n0=total_fixed+2*total_orbits
    n2=last_layer
    n1=total_states-n0-n2
    assert all(z>=0 for z in [n0,n1,n2]);assert n0+n1+n2==total_states
    return total_fixed,total_orbits,n0,n1,n2,osc_basin

if __name__=='__main__':
    for m in range(1,31):
        result=check(m)
        if m in (1,2,3,4,5,6,12,30):print('m',m,'fixed,orbits,entry0,1,2,osc-basin',result)
    print('PASS independent multinomial reconstruction and boundary cases for m=1..30')
