import sys
sys.path.insert(0, 'work')
from pg213 import INC, LINES, NPTS, NL, check_blocking, check_minimal, check_nontrivial
# the three minimized 21-sets found
sets={
 'T16':[1, 6, 16, 21, 26, 49, 61, 69, 78, 79, 82, 93, 102, 108, 109, 112, 129, 138, 143, 163, 171],
 'T37':[0, 9, 21, 35, 42, 59, 65, 77, 78, 100, 103, 114, 126, 142, 143, 168, 169, 170, 174, 180, 181],
 'T39':[16, 17, 20, 26, 28, 31, 32, 43, 77, 79, 88, 89, 153, 164, 165, 168, 171, 173, 180, 181, 182],
}
def name(p):
    if p<169: return f"({p//13},{p%13},1)"
    if p<182: return f"(1,{p-169},0)"
    return "(0,1,0)"
for k,S in sets.items():
    b,n,u=check_blocking(S); mn,miss=check_minimal(S); nt=check_nontrivial(S)
    print(k,"blocking",b,"unblocked",n,"minimal",mn,"nontrivial",nt)
    print("  pts:",[name(p) for p in S])
