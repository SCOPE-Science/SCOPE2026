# Independent mathematical audit

## correctness

PASS

Each character weights the edge subset by the product of its edge signs, and the rooted-forest determinant counts each acyclic subset with its full product of component sizes. The polynomial identity allows signed weights; incidence-minor expansion also gives it by dropping one row in each tree component. Eliminating the n diagonal pivots 3,1,1,-1 gives the claimed Schur matrix and prefactor. With s=b+c and e=b-c the scaled determinant H factors as (1+a-2s-d)(3+a+3d)-3e², agreeing with the stated expansion. The counting convolution is diagonal in the unnormalized Walsh convention with these exact eigenvalues, and column multiplicities are multinomial, so its nullity and rank follow. Modulo two all sign choices give the unsigned value (n+1)(n+3)3^{n-1}, odd for even n. On odd n=2k+1 the type (k,0,0,k+1) zeros the first factor, giving the stated lower bound. At weight two the same-column, same-shore distinct-column, and opposite-shore distinct-column values of H are (n-1)(n+5), n²-4n-17, and (n-5)(n+1), respectively. Weight one gives n²-7 and weight zero is positive. Thus only the opposite-shore distinct-column case at n=5 is singular among these degrees, with exactly 20 such frequencies.

## originality

PASS

The signed forest determinant and Walsh convolution machinery are established. The checked claim is the explicit edge-spectrum evaluation together with global invertibility and the exact degree-two exception. The strongest same-graph and same-family indexed results use materially different kernels; neither yields those classifications. The judgment is bounded to the sources checked, not a priority inference from record dates.

## value

PASS

The natural observable is the spectrum of convolution by the actual rooted-forest counting measure, retaining labeled edges and root multiplicity. The parity law resolves recovery on the full edge signal space; the unique width-five resonance distinguishes recovery of two-edge components from full invertibility and specifies exactly which components are lost there. The evaluated spectrum and type multiplicities are reusable for ranks without enumerating all labeled frequencies. These are structural facts, not a determinant restatement or a finite list of computed examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
