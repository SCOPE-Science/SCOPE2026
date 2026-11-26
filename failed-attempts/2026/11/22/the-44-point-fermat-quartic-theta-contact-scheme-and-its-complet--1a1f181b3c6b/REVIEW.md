# Independent mathematical audit

## correctness

PASS

I classified bitangents independently by asking when the restricted binary quartic is a square up to scalar over the algebraic closure. A line with one nonzero coefficient leaves two fourth powers and cannot give a square. For a line with two nonzero coefficients, the same binary-quartic test forces the coefficient of one fourth power to vanish, giving exactly the 12 coordinate-pair hyperflexes; the four roots on each disjoint chart are simple. For a line X+aY+bZ=0 with ab nonzero, set S=aY and T=bZ. The restricted quartic has coefficients (1+a^-4,4,6,4,1+b^-4). Comparing to (A S^2+B ST+C T^2)^2 gives A=C and AB=2. The middle coefficient gives (A^2-1)(A^2-2)=0; A^2=1 is impossible, so a^4=b^4=1. The quadratic has nonzero discriminant in characteristic >=5, giving two distinct contacts per line, and smoothness makes the tangent at each point unique. In the chart Z=1, the two fourth powers u,v of an ordinary contact are the two roots of t^2+t+1, in either order. This follows by substitution in the squared restricted form and is exactly the system u+v=-1, uv=1 defining the proposed second scheme; no coordinate vanishes there. Its Jacobian in u,v is nonsingular since u!=v, and the fourth-power map is etale on the torus. Thus there are exactly 32 reduced points, and both schemes are finite etale and disjoint. In a cyclic group of order q-1, each primitive cube root has gcd(4,q-1) fourth roots if 3 divides q-1, otherwise neither primitive cube root exists. This gives 2 gcd(4,q-1)^2 or zero ordinary points. Hyperflexes give 12 iff 8 divides q-1, and the line count adds gcd(4,q-1)^2 to that. All q odd prime to 3 satisfy q^2=1 mod 24, so the exponent of the quadratic Euler factor is exactly (44-f_q)/2, and the splitting degree is one only in the 44-fixed-point case. Independently enumerated all base-field lines by their binary-quartic square test and all contact points via the tangent gradient in eight prime fields, one per residue (python3 /workspace/audit_evidence/fermat.py). All three columns matched; the all-prime-power conclusion rests on the symbolic proof. No statement is made in characteristics two or three.

## originality

FAIL

The frozen finding does not establish the complete arithmetic contact spectrum as a distinct result relative to the materially broader indexed Ciani-pencil classification. That distinct entry explicitly claims an exact Frobenius cycle decomposition of the same reduced support for every smooth member in the same characteristic range. In the symmetric Ciani pencil x^4+y^4+z^4+t(x^2y^2+y^2z^2+z^2x^2), the Fermat member is t=0 and is smooth in this range. The indexed all-smooth-members claim therefore covers the core arithmetic contact data at statement level, not just a coincident example or the bitangent-line fields. Same-day publication does not settle priority. The indexed description does not reproduce the degree-eight complete-intersection equation, and this review does not find that particular equation already stated. The frozen central assertion joins the scheme and complete arithmetic spectrum without a distinct focal claim confined to the equation. This is a scope/overlap decision on the actual submitted result, not a negative verdict based on access failure.

## value

FAIL

A coordinate model of a reduced tangency locus and the distinction between rational lines and rational contacts are meaningful. The frozen value argument, however, is for the complete arithmetic census and its consequences, which the broader all-members contact result already covers at the stated scope. Beyond that coverage, the remaining proposed increment is a specific symmetric presentation of the ordinary support. The frozen record does not establish and motivate a distinct stand-alone scheme-theoretic problem beyond expressing the same classified support in these coordinates. This does not deny possible independent utility of such a presentation if supported as a narrower finding; no such repair is delivered here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
