# Independent mathematical audit

## correctness

PASS

For every m>0, the norm has weight W(t)=exp(-t^{m/2}) and moments m_j=(2/m)Gamma((2j+2)/m), giving the exact input K(m)^2=Gamma(4/m)/Gamma(2/m) by published Theorem 1.3. Put x=2/m: duplication gives K(2/x)^2=2^{2x-1}Gamma(x+1/2)/sqrt(pi). The log derivative is 2 log2+psi(x+1/2), derivative psi1>0, initial value -gamma<0 and limit +infinity, hence one strict global minimizer. Conversion to m reverses derivative signs correctly. Small-x log-Gamma expansion gives K(m)=(1/sqrt2)[1-gamma/m+(gamma^2+pi^2)/(2m^2)+O(m^-3)], approached from below; Stirling gives divergence as m->0. Independent 55-digit mpmath root returned x=0.1450347431666722513354589782140, m=13.7897993014103048741, K=0.69348357463966042675. Finite numerics corroborate, not prove, universal claims.

## originality

FAIL

A primary published theorem already gives the entire exact Korenblum-radius function for every m>0; the assessed sign reversal, numerical minimum and endpoints follow by ordinary differentiation and gamma expansions. Additional universal radial theorem independently gives the same complete function. Formula-to-claim implication is decisive even if derivative and numbers are not separately printed.

## value

FAIL

The exponent family and its exact radius are natural, and the nonmonotone reversal is mathematically true. However the entire sharp-radius function K(m) was already printed for all m>0. The assessed classification is only one derivative of that explicit Gamma formula plus standard log-convexity and gamma endpoint expansions, with no new Korenblum inequality, weight class, boundary phenomenon not forced by published exact data, or independent structural lemma. The numerical optimum is an incidental decimal of the already-determined exact curve. This is routine special-function calculus, not a separate motivated unknown invariant or substantial new classification under the shared value standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
