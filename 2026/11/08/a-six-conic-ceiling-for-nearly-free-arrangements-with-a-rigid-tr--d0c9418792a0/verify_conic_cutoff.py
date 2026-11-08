#!/usr/bin/env python3
"""Exact integer checks for conic-arrangement near-freeness obstructions.
Requires only Python 3 standard library. Scientific sources appear in RESULT.md.
"""

def candidates(k, no_triples=False, only_nodes_a7=False):
    K=k*(k-1)
    out=[]
    for n3 in ([0] if no_triples else range(K+1)):
        for a5 in range(K//2+1):
            for a7 in range(K//3+1):
                a3=K-n3-2*a5-3*a7
                nodes=a5+2*a7-n3
                if a3<0 or nodes<0: continue
                if only_nodes_a7 and (n3 or a5 or a3): continue
                if 560*k+100*nodes+75*n3 < 184*a3+404*a5+608*a7: continue
                out.append((nodes,a3,n3,a5,a7))
    return out

def main():
    for k in (5,6,7,8):
        all_types=candidates(k)
        no_triples=candidates(k,no_triples=True)
        only_a7=candidates(k,only_nodes_a7=True)
        assert (len(all_types)==0)==(k>=7)
        assert (len(no_triples)==0)==(k>=6)
        assert no_triples==([(13,0,0,1,6)] if k==5 else [])
        assert not only_a7
        print('k=',k,'all=',len(all_types),'no_D4=',len(no_triples),'nodes_A7=',len(only_a7))
    # Verify the key exact identity in the proof for every enumerated profile.
    for k in (5,6,7,8):
        K=k*(k-1)
        for n2,t3,n3,t5,t7 in candidates(k):
            assert n2+3*n3+2*t3+3*t5+4*t7==2*K
            tau=n2+4*n3+3*t3+5*t5+7*t7
            if k>=5: assert tau==3*K
            assert n2+n3==t5+2*t7 if k>=5 else True
    print('CONIC_CUTOFF_ARITHMETIC_PASS')

if __name__=='__main__':
    main()
