# Independent mathematical audit

## correctness

PASS

The phase diagram and optimizer characterization in the Finding follow independently by completing the penalized cost. For theta=lambda-j>0 and B the actual expected score energy, J-lambda B = sigma^2(h-lambda+g^2/theta) - (2theta-a-b^2/theta) E[u_0^2] - theta E[(u_1-g x_1/theta)^2]. Put theta_0=(a+d)/4. For theta>=theta_0 this is an upper-bound certificate; equality requires using the full budget, the stated feedback, and s=0 if theta>theta_0. With s=0 the budget requires theta=b sigma/sqrt(beta-sigma^2), which is at least theta_0 precisely through beta_crit. At theta_0 the remaining affine budget identity determines s uniquely, including s=0 at equality; any independent initial input with that second moment works. Substitution gives both value branches, their common derivative at equality, and the exact gap above it, theta_0 (sqrt(beta-sigma^2)-b sigma/theta_0)^2. The exact witness follows at h=3,j=1,b=1,sigma^2=1,beta=3. One auxiliary sentence at RESULT.md line 113 is off by equality: the strictly regular Riccati family cannot saturate at beta=beta_crit either, as the preceding displayed strict inequality already shows. It approaches the optimum there as a limit. This wording error does not enter or invalidate the Finding, which treats threshold equality correctly.

## originality

FAIL

The scalar formulas are not printed in the closest prior paper, but they result mechanically from its exact oracle and singular Riccati prescription. Section IV already supplies the active constraint, regular recursion and boundary null-direction solution for this very optimization. Specializing to two scalar steps leaves only a terminal gain, one scalar quadratic equation for the boundary, and an affine budget balance. The no-excitation comparator is the prior regular step with the initial control fixed to zero. Thus the claimed phase diagram is covered by implication, not by a word-for-word match or a database miss.

## value

FAIL

The quantified example is a useful illustration of the known singular-budget mechanism, but the proposed invariant is the direct two-step scalar evaluation of the existing solution, and the restricted-policy gap is the square produced by the same one-step calculation. No additional nonmechanical policy obstruction, oracle theorem, or link to the outer nonlinear criterion is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
