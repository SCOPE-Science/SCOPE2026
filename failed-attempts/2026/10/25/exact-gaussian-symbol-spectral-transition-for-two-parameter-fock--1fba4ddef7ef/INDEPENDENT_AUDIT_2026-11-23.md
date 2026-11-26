# Independent mathematical audit

## correctness

FAIL

The integral in the Finding and the absolute-convergence claim in Assumptions (RESULT.md lines 8–11, 30, 35) are false on part of the stated domain. Take f=K_0=1, output point z=0, and w=x+iy. The modulus of the integrand including Gaussian weight is (π√s)^(-1) exp[-(r+t/(2s))x²-(r-t/(2s))y²]. It is integrable if and only if r>t/(2s), and diverges even at equality (e.g. s=2,t=1,β=3/4). Thus for 1-t/(2s)≤β<1 the submitted Lebesgue integral does not define the prescribed map on the kernel span, so calling that map unbounded is not correct. The critical r satisfies r_*²=t/s+(1-t/s)/H>t/s, so the compact regime and endpoint, and a nonempty supercritical interval, remain inside the convergence domain. There, the independent algebra check recovered the stated Gram coefficients, the squeezed-eigenvalue and generating-function identities, the exact trace agreement, and the endpoint normalization; the harmonic-oscillator reduction below also supplies a complete eigenbasis. For well-defined supercritical β, imaginary normalized kernels diverge in norm. CHECK.py was inspected only: it symbolically checks the threshold simplification and uses floating point for five samples plus endpoint coefficients; it does not check integrability, all-domain realization, or completeness. One could restrict the integral range or separately define a formal coherent-kernel prescription, but the latter is not the given absolutely convergent integral.

## originality

FAIL

In the corrected domain the exact coherent kernel action, squared-norm diagonal (hence full polarized Gram form), and blowup threshold are already encoded in Dong–Wang–Zhu, Lemma 1 and Proposition 14. The compact-spectrum calculation and the endpoint are direct applications of the standard Weyl normal form for that already known diagonal Gaussian, as shown below. The weighted operator need not itself be canonical: its compact-regime Gram operator is also a scaled unweighted canonical Gram operator after reparametrization. No separate spectral mechanism survives the comparison.

## value

FAIL

The operator family is well motivated, and the endpoint model would be useful to an analyst looking up this example. Once the already published exact coherent diagonal is used, however, the proposed contribution is an instance of standard Gaussian Weyl spectral formulas and a multiplication-by-symbol boundary, with a false additional convergence range. Correcting the domain recovers a useful exposition, not a surviving independently valuable unknown claim under the stated standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
