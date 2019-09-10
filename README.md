# Portfolio of `numpy`, `pandas`, and `matplotlib` use cases

This repository serves as a collection of modules built on top of `numpy`, `pandas`, and
`matplotlib`. These correspond to solutions I have worked on in the past.

## Setup

The following apply for the local modules only.

### System requirements

* `make`
* `python (>=3.6)`

### Installation for local

```
$ make install
```

This installs the Python virtual environment that can be activated with

```
$ source venv/bin/activate
(venv) $
```

## Contents

### Local

* [traces](np-pd-portfolio/traces.py): A method to find the traces of arbitrary
  planar points on a given line within that plane.

### External

* [Processing a heterogeneous feature matrix with pandas][fm-pd]
* Various utilities (from [dx-utilities][]):
  * [Linear algebra][linear-algebra]
  * [Integrals][]
  * [Array interface][array-interface]
* From [dx-punch](https://gitlab.com/d-e/dx-punch)
  * [A postprocessor based on `matplotlib` and `pandas`][dx-punch-postprocessor]

[fm-pd]: https://github.com/kodemartin/json-feature-matrix-processor
[dx-utilities]: https://gitlab.com/d-e/dx-utilities
[array-interface]: https://gitlab.com/d-e/dx-utilities/blob/master/dx_utilities/array_interface.py
[linear-algebra]: https://gitlab.com/d-e/dx-utilities/blob/master/dx_utilities/linear_algebra.py
[integrals]: https://gitlab.com/d-e/dx-utilities/blob/master/dx_utilities/integrals.py
[dx-punch-postprocessor]: https://gitlab.com/d-e/dx-punch/blob/master/dx_punch/EC2/slab.py#L390
