# Independent mathematical audit

## correctness

PASS

Each source one covers a clipped interval of output positions. For an interior one-run [a,b], the preceding and following output zeros force the first and last markers at a+h-1 and b, so L=b-a+1>=h is necessary. In between the markers the criterion is gaps at most h, giving the composition count c_h(L-h), including the coincident-marker case. A leading one-run of length a followed by a zero forces the source one at a; the preceding a-1 bits must avoid h zeros, and reversal handles the trailing run. Output-zero windows fix the other bits and separate the choices. An all-one output has exactly the source words with no h zeros and always at least two such words; all-zero has a single source. Therefore singleton outputs have boundary lengths 0 or 1 and interior lengths h or h+1, since compositions of d>=2 include both all ones and a part 2. For outputs with a zero the unambiguous grammar is E Z (I Z)* E, with Z=z/(1-z); use E=1/(1-z), I=z^h/(1-z) for reachability, E=1+z, I=z^h+z^(h+1) for uniqueness. Adding all-one outputs and the empty convention yields the claimed series. The source's shortcut from eventual coefficient positivity to a unique dominant pole is insufficient in isolation. Here the exact denominators suffice: at |z|<=rho_R, |1-z|>=1-|z|, with strict inequality at other points of |z|=rho_R, so (1-z)^2=z^(h+1) cannot vanish elsewhere in that disk. For U, equality in |z+z^(h+1)+z^(h+2)|<=rho_U+rho_U^(h+1)+rho_U^(h+2)=1 at a root forces z positive. Both positive roots are simple and give positive leading coefficients by the local simple-pole formula. The U denominator at rho_R is rho_R^2(1-rho_R)>0 and decreases strictly to its positive zero. Thus the claimed strict exponential ratio holds at every fixed h, with no width uniformity asserted.

## originality

PASS

The Boolean dilation interpretation, standard run grammars and exact nearest-neighbor cellular-automaton preimage counting are known ingredients. Credit the all-width finite-linear unrestricted image and singleton spectra together with their strict growth-rate comparison, not the generic idea of preimage enumeration or the width-three count. The strongest distinct indexed match uses a different domain and boundary, and the closest inspected primary preimage formula covers the width-three special case, not the full pair of spectra.

## value

PASS

The exact enumerations distinguish two operationally different notions for a natural ordered sensor: a largest noiseless distinguishable codebook can select one representative per reachable output, but a singleton fiber decodes without imposing a codebook. The uniform-in-length formulas and strict fixed-width exponential gap explain why those two populations differ substantially; the full run-dependent list sizes make the result useful even when neither count alone suffices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
