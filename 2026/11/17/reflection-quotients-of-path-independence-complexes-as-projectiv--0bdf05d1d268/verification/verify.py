"""Independent finite checks for reflection orbit models of path independence complexes."""

def independent_masks(n):
    masks=[0]
    for i in range(n):
        masks+= [m|(1<<i) for m in masks if i==0 or not (m&(1<<(i-1)))]
    return masks

def reverse(mask,n):
    out=0
    for i in range(n):
        if mask>>i&1:out|=1<<(n-1-i)
    return out

def dimensions(n):
    if n%3==1:return None
    k,r=divmod(n,6)
    if r==0 and k>=1:return k,k
    if r==2:return k,k+1
    if r==3:return k+1,k
    if r==5:return k+1,k+1
    raise ValueError(n)

def euler(masks):
    return sum((-1)**(m.bit_count()-1) for m in masks if m)

def fixed_euler(n):
    orbits=[((1<<i)|(1<<(n-1-i))) for i in range(n//2)]
    if n%2:orbits.append(1<<(n//2))
    result=0
    for mask in range(1,1<<len(orbits)):
        original=0
        for j,orb in enumerate(orbits):
            if mask>>j&1: original|=orb
        if not (original & (original<<1)):
            result+=(-1)**(mask.bit_count()-1)
    return result

def expected_chi(n):
    ab=dimensions(n)
    if ab is None:return 1,1,1
    a,b=ab
    chi_original=1+(-1)**(a+b-1)
    chi_fixed=1+(-1)**(a-1) if a else 0
    return chi_original,chi_fixed,(chi_original+chi_fixed)//2

def verify_fold(n,faces):
    bad=(1<<2)|(1<<(n-3))
    out1=1
    out2=1<<(n-1)
    face_set=set(faces)
    for mask in faces:
        output=(mask&~bad)|(out1 if mask&(1<<2) else 0)|(out2 if mask&(1<<(n-3)) else 0)
        assert output in face_set,(n,mask,output)
        assert (mask|output) in face_set,(n,mask,output,'contiguity')
        assert not output&bad
        mask_r=reverse(mask,n)
        output_r=(mask_r&~bad)|(out1 if mask_r&(1<<2) else 0)|(out2 if mask_r&(1<<(n-3)) else 0)
        assert output_r==reverse(output,n),(n,mask,'equivariance')

for n in range(2,25):
    faces=independent_masks(n)
    if n>=6:verify_fold(n,faces)
    actual_chi=euler(faces)
    actual_fixed=fixed_euler(n)
    original,fixed,quotient=expected_chi(n)
    assert (actual_chi,actual_fixed)==(original,fixed),(n,actual_chi,actual_fixed,original,fixed)
    assert (actual_chi+actual_fixed)%2==0
    if n in [2,3,5,6,8,11,12,14,17,18,20,24]:
        print('n=%d: representation=%s, chi_original=%d, chi_fixed=%d, chi_quotient=%d, faces=%d'%(n,dimensions(n),original,fixed,quotient,len(faces)))
print('ALL_FINITE_CHECKS_PASSED: n=2..24; equivariant contiguous retractions n=6..24')
