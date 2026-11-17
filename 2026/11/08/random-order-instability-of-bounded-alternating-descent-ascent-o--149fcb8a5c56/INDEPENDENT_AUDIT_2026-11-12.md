# Independent mathematical audit

## correctness

PASS

The x-then-y and y-then-x complete-sweep matrices A=[[1,-t],[t,1-t²]] and B=[[1-t²,-t],[t,1]] have determinant 1, elliptic trace 2-t² for 0<t<2, and distinct positive quadratic invariants W with ±t/2 cross terms, proving each fixed order is power bounded. Exact average (AᵀA+BᵀB)/2=(1+t⁴/2)I gives all-n balanced mean-square growth. For mixed p∈(0,1), the 3D covariance map has det(I−L_p)=−8p(1−p)t⁶<0, hence spectral radius r>1. A positive resolvent provides a nonzero PSD adjoint eigenmatrix; a rank-one eigenmatrix would force a real invariant line of elliptic Aᵀ, impossible, so it is PD. Comparing min/max eigenvalues gives E||z_n||²≥c r^n||z0||² for every deterministic nonzero start. Independently checked the matrix and determinant symbolic identities. The endpoints p=0,1 and t=2 excluded appropriately.

## originality

PASS

Zhang–Yu and related alternating-gradient papers handle fixed order or different player sampling. Crucial implication correction: the November 2 published paired symplectic-Euler paper concerns matrices conjugate by a sign flip to these Gauss–Seidel maps, and its exact fair-marginal two-step block multiplier with independent orientations r=1/4 gives (1+t⁴/2)^2. Thus the highlighted fair energy factor is not a separate new result. The surviving exact every-interior-bias sign certificate plus positive-definite eigenmatrix proving growth for every nonzero deterministic start are not supplied by that fair-marginal paired theorem, nor by the inspected fixed-order optimization literature. This narrow but meaningful remainder is the originality basis; equivalent specialist all-bias results remain a risk.

## value

PASS

The practically motivated question is whether random full-sweep player order preserves the power boundedness of either deterministic alternating method. The all-bias theorem answers sharply for every normalized elliptic step and every initial vector, establishing no safe interior mixing law. Despite previously known fair energy inflation, the uniform all-bias classification and its explicit covariance sign certificate are a meaningful structural obstruction, not solely a renaming or easy tiny gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
