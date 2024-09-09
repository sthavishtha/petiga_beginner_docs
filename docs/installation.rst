.. role:: envvar(literal)
.. _installation:

Installation
============

Instructions for installing both PETSc and PetIGA on `Bridges2`_ cluster are provided here.

PETSc
-----

1. Download `PETSc`_

2. Load required modules on the cluster::

      module load gcc/10.2.0 openmpi/4.0.5-gcc10.2.0
      module load mkl

3. Set optimization flags. Tune the optimization flags as per your requirements.::

      OPTFLAGS="-O3"

4. Configure PETSc on bridges2 with the appropriate options. Below is an example::

      ./configure --with-cc=mpiicc --with-cxx=mpiicpc --with-fc=mpiifort --download-sowing-cc=mpiicc --download-sowing-cxx=mpiicpc --with-scalar-type=real --with-shared-libraries=0 --with-debugging=no --with-blas-lapack-dir=$MKLROOT --with-scalapack-lib="-L$MKLROOT/lib/intel64 -lmkl_scalapack_lp64 -lmkl_blacs_openmpi_lp64" --with-scalapack-include=$MKLROOT/include COPTFLAGS="$OPTFLAGS" CXXOPTFLAGS="$OPTFLAGS" FOPTFLAGS="$OPTFLAGS" --download-metis --download-parmetis --download-spooles --download-superlu_dist=yes PETSC_ARCH=<arch_name>

5. Compile PETSc: Once the configuration is complete, follow the output instructions to finish compiling the library.

6. Set environment variables: Save the environment variables :envvar:`PETSC_DIR` and :envvar:`PETSC_ARCH` into your :envvar:`.bashrc` so that they are always set in your environment.

7. Verify installation::

      make PETSC_DIR=<path_to_petsc> PETSC_ARCH=<arch_name> check


PetIGA
------

1. Download `PetIGA`_

2. Set the :envvar:`PETIGA_DIR` environment variable to the correctly downloaded location and change to the appropriate directory::
   
      cd $PETIGA_DIR

3. Compile PetIGA::

      make PETSC_DIR=<path_to_petsc> PETSC_ARCH=<arch_name> all

4. Verify installation::

      make PETSC_DIR=<path_to_petsc> PETSC_ARCH=<arch_name> test   

.. _Bridges2: https://www.psc.edu/resources/bridges-2/
.. _PetIGA: https://github.com/dalcinl/PetIGA
.. _PETSc: https://www.mcs.anl.gov/petsc/

.. Local Variables:
.. mode: rst
.. End:
