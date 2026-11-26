# Independent mathematical audit

## correctness

PASS

With q₀=e_r and positive subdiagonals, q₁ has entries −w_ri/b₀ only at neighbors. Multiplication by L and subtraction of the q₀ and q₁ components gives q₂,i=−w_ri(d̂_ri−a₁)/(b₀b₁) at a neighbor, q₂=0 at the root and beyond distance two, and a positive sum of two-edge conductance products divided by b₀b₁ at distance two. This accounts for triangles with the claimed minus sign in d̂. S=diag(1,−1,1) makes K=−ST₃S irreducible Metzler, so e^(tK)e₁ is strictly positive for t>0. This proves the non-neighbor conclusions and makes the smallest-Ritz coefficient at a neighbor a positive multiple of H, by the last row of K's positive top eigenvector. The neighbor response vanishes initially with derivative w_ri>0 by degree-one Lanczos exactness. To independently check the entire time classification, write the eigenvalues θ₀<θ₁<θ₂. After multiplying the response by e^(θ₂t), initial vanishing gives A(e^(at)−1)+B(e^(bt)−1), with a=θ₂−θ₀>b=θ₂−θ₁>0 and sign A=sign H. The ratio (e^(at)−1)/(e^(bt)−1) is strictly increasing from a/b to infinity: it is the average of the strictly increasing (a/b)e^((a−b)s) under weight b e^(bs) on [0,t]. Dividing by e^(bt)−1, the sign is therefore the sign of a function starting at (Aa+Bb)/b>0, decreasing to minus infinity precisely if A<0, and positive throughout if A≥0. This proves strict positivity even at equality and rules out any return. The initial value handles t=0; exact early termination follows from Krylov invariance. Independent replay with python3 /workspace/evidence/lanczos_witness.py orthonormalizes the raw power basis, reproduces all five frozen Lanczos coefficients and the cubic, and verifies by Sylvester's criterion T₃−I≻0 and det(2I−T₃)>0, hence 1<θ₀<2. It recovers 61−a₁−a₂=215528/138043>0 and a₁+a₂−2>40. The other two source neighbors are therefore positive while neighbor 1 eventually turns negative. The numerical crossing 0.1181626757546 and negative value near −0.0011882008 at 0.2 are illustrations, not the sign certificate. The exact heat kernel is positive by connected irreducible Metzler positivity.

## originality

PASS

The supported distinct content is the all-graph original-coordinate sign classification at depth three, including the exact all-time inequality and the single irreversible crossing. Classical projection, approximation guarantees and reduced-coordinate positivity, and the common local Krylov support mechanism are not claimed as new. The strongest comparison is a third-iterate shifted-inverse sign law on trees; its algebra is closely related but its proved statement does not cover the claimed time-dependent graph heat theorem.

## value

PASS

For an ordinary truncation of graph heat from a point source, the exact kernel is positive but the low-depth approximation need not be. The exact local threshold tells whether any specified coordinate will fail, and distinguishes a permanent late-time failure from a transient artifact. Including equality, triangles, exact breakdown, and an exact small weighted witness gives a usable mathematical diagnostic rather than an isolated numerical sign counterexample. The claim is not finite-precision assurance or a result for arbitrary depth.

The dated certificate retains the supplied scientific assessment, sources and limitations.
