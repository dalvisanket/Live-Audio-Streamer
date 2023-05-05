
@ECHO OFF
FOR /L %%A IN (1,1,1) DO (
    start /B python throughput.py
)

timeout /T 25 /NOBREAK > NUL

@ECHO OFF
FOR /L %%A IN (1,1,5) DO (
    start /B python throughput.py
)

timeout /T 25 /NOBREAK > NUL


@ECHO OFF
FOR /L %%A IN (1,1,10) DO (
    start /B python throughput.py
)

timeout /T 25 /NOBREAK > NUL


@ECHO OFF
FOR /L %%A IN (1,1,20) DO (
    start /B python throughput.py
)

timeout /T 25 /NOBREAK > NUL

@ECHO OFF
FOR /L %%A IN (1,1,35) DO (
    start /B python throughput.py
)

timeout /T 25 /NOBREAK > NUL

@ECHO OFF
FOR /L %%A IN (1,1,50) DO (
    start /B python throughput.py
)

timeout /T 25 /NOBREAK > NUL


@ECHO OFF
FOR /L %%A IN (1,1,75) DO (
    start /B python throughput.py
)

timeout /T 25 /NOBREAK > NUL


@ECHO OFF
FOR /L %%A IN (1,1,100) DO (
    start /B python throughput.py
)

timeout /T 25 /NOBREAK > NUL


