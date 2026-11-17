# Independent mathematical audit

## correctness

PASS

The finite binary host W=(0^r1)^k, r>=2,k>=1, has a greedy prefix/last-symbol absence/bridge test for minimal absent scattered subsequences. The claimed reachable automaton states A_1...A_r,D,B and their boundary crossing transitions classify the language without double-counting; weighted path equations eliminate to F_r(z,t)=zt(t^r+2t-2t^(r+1)z+2t^(r+2)z)/(1-(t+t^r)z+(t^(r+1)-t^(r+2))z^2). Setting t=1 gives 3z/(1-2z), hence 3*2^(k-1). Independently brute-forced candidate minimal absent words for representative r=2,3,4 and small k, reproducing exact length spectra. Finite checks support but do not replace the all-parameter state proof.

## originality

FAIL

The exact total 3*2^(k-1) and the complete minimal absent word language are already covered by an earlier published Resultary result on (0^a1^b)^k for all a,b,k. Take a=r>=2, b=1 in its explicit complete-language criterion and its exactly-one-singleton-run case. That prior characterizes each word, including its length, so the new rational length GF is a weighted enumeration of an already complete classification, not an independent genuinely unclassified structure. Within-day priority between two November 8 publications was not established; this is a claim-coverage decision, not a chronological attribution.

## value

FAIL

The natural periodic-word MAS invariant is mathematically motivated, but the final claimed classification and its total are a strict special case of the already published complete-language theorem, and the bivariate expression only enumerates the earlier specified words by length. There is no separately motivated new obstruction or invariant beyond this covered family. This is a scientific-value rejection, not a proof defect.

The dated certificate retains the supplied scientific assessment, sources and limitations.
