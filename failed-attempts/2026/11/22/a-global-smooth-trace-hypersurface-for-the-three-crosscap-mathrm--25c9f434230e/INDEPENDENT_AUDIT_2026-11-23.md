# Independent mathematical audit

## correctness

PASS

At c=0, C²=-I and A²B²=-I. If a≠0, commuting with B²=-A^(-2) gives [B,A²]=0 and then [B,A]=0 by Cayley–Hamilton; if a=0 then B²=I and det B=1 force B=±I. Thus Z=AB has Z²=-I, and writing A in the centralizer span{I,Z} gives A=(aI+bZ)/2 and B=(bI+aZ)/2 with a²+b²=4; these formulas conversely realize every pair on that conic. Fixing Z=diag(i,-i), the centralizer torus has invariant ring C[t,vw]/(vw+1+t²)=C[t] on the traceless C slice, with s=2it. The reduction to the torus slice is regular by the homogeneous-space description of the conjugacy class of Z; the asserted global ring also directly verifies the reduced boundary scheme. For c≠0, the companion matrices have tr(AB)=(a-t)(b-t)+2 and determinant one. With D=(A²B²)^(-1) the trace constraint gives tr D+2=c²; det(I+D)=tr D+2 and (I+D)²=(tr D+2)D, so C=(I+D)/c works even at a=0 or b=0. Independently, tr(ABC²)=tr(AB) by cyclic permutation and inversion, hence cs=2p without any division; cyclically permuting A,B,C proves the other two identities globally. Goldman's seven trace generators descend surjectively by exactness of reductive invariants over C. The linear polynomial F in s is primitive because none of a,b,c divides its constant coefficient in s. Realizing D(c) in the irreducible hypersurface forces zero kernel, and the partial in s forces abc=0 at any putative singular point; the other two corresponding trace partials then force a=b=c=0, impossible. VERIFY.py and requirements.txt were read without executing the script. The verification is limited to the reduced complex affine GIT quotient, not a scheme or stack with additional structure.

## originality

FAIL

The proposed global result is a direct corollary of the already proved identities and generic chart for the exact same object, not a new gluing theorem. Crucially, the equality cs=2p in Chen §4 is proved by trace manipulation without division. Applying that calculation to the cyclically reordered triples gives as=2q and bs=2r everywhere. Even if one uses only Chen's stated generic chart rather than the undivided calculation, its dense image and reducedness extend all three polynomial equalities to the full quotient. These identities eliminate the pair traces in the classical seven-coordinate affine embedding, so the closure of the known dense chart determines the claimed global presentation. No earlier print occurrence of the exact four-trace equation is needed for this implication. The matrix boundary argument is an alternative verification of a boundary already separately covered, not a surviving novel part of the frozen claim.

## value

FAIL

The four-coordinate formula is convenient and the proof is a readable synthesis. As a standalone new mathematical result, however, the alleged gluing gap disappears after applying Chen's undivided trace computation cyclically in the existing closed trace embedding. The only remaining steps are reduced closure, a one-line Jacobian check and the already separately classified cylinder; there is no further substantive claim in the frozen record beyond this routine deduction. This does not detract from the usefulness of the formula as an exposition of consequences of the prior work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
