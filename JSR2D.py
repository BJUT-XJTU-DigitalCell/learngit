import numpy as np
from math import sqrt
from GLOBALCA import AVERAGE_CCA, CA_CURRENT

global B_WALL, B_INFLOW, B_OUTFLOW, B_SYMMETRY, B_SOURCE, PMAX, EMAX, NVEX, MAX_NITERATION, UNITEC, MOLNUM
B_WALL = 1
B_INFLOW = 2
B_OUTFLOW = 4
B_SYMMETRY = 8
B_SOURCE = 16
PMAX = 50000
EMAX = 100000
NVEX = 3
MAX_NITERATION = 1000
UNITEC = 1.610217733
MOLNUM = 6.0221367

global NP, NE, NPOCH, NOD, NOE, PX, PY
global CTRL_AREA, TOTAL_AREA
NP = 0
NE = 0
NPOCH = np.empty(PMAX, int)
NOD = np.empty([NVEX, EMAX], int)
NOE = np.empty([NVEX, EMAX], int)
PX = np.empty(PMAX, float)
PY = np.empty(PMAX, float)
CTRL_AREA = np.empty(PMAX, float)
TOTAL_AREA = 0.0

global EFVM, PFVM, BFVM, AFVM, CFVM
EFVM = np.empty([3, EMAX], float)
PFVM = np.empty(PMAX, float)
BFVM = np.empty(PMAX, float)
AFVM = np.empty(PMAX, float)
CFVM = np.empty(PMAX, float)

global CCAJSR, NEWCCA, MEDCCA, RITER, PITER, APK
CCAJSR = np.empty(PMAX, float)
NEWCCA = np.empty(PMAX, float)
MEDCCA = np.empty(PMAX, float)
RITER = np.empty(PMAX, float)
PITER = np.empty(PMAX, float)
APK = np.empty(PMAX, float)

global DT, NSTEP, ILOAD, RELEASE_TIMES
global DSAVE
DT = 2 * 10 ** -6
NSTEP = 50000
ILOAD = 1
RELEASE_TIMES = 2 * 10 ** -2
DSAVE = 100

global KDCSQ, DCAJSR, BCSQ, H_JSR
global CCAMYO, DCARYR
global CCAFSR, DCAFSR

CCAFSR = 1.0
CCAMYO = 0.0001
BCSQ = 14.0
KDCSQ = 0.63
H_JSR = 30.0
DCAJSR = 3.5 * 10 ** 8
DCARYR = 6.5 * 10 ** 7
DCAFSR = 0.7854 * 10 ** 6

global ICARYR, ICAFSR, AVG_CA_JSR
ICARYR = 0.0
ICAFSR = 0.0
AVG_CA_JSR = 0.0


def MAIN():
    LOAD_GRIDINFO()
    INITIAL_PARAMETER()
    COEFFICIENT()
    DOLOOP_DIFFUSION()


# *************************
def INITIAL_PARAMETER():
    # INCLUDE 'T0.INC'

    # B_WALL = 1
    # B_INFLOW = 2
    # B_OUTFLOW = 4
    # B_SYMMETRY = 8
    # B_SOURCE = 16
    # PMAX = 50000
    # EMAX = 100000
    # NVEX = 3
    # MAX_NITERATION = 1000
    # UNITEC = 1.610217733
    # MOLNUM = 6.0221367
    global B_WALL, B_INFLOW, B_OUTFLOW, B_SYMMETRY, B_SOURCE, PMAX, EMAX, NVEX, MAX_NITERATION, UNITEC, MOLNUM
    # NP = 0
    # NE = 0
    # NPOCH = np.empty(PMAX, int)
    # NOD = np.empty([NVEX, EMAX], int)
    # NOE = np.empty([NVEX, EMAX], int)
    # PX = np.empty(PMAX, float)
    # PY = np.empty(PMAX, float)
    # CTRL_AREA = np.empty(PMAX, float)
    # TOTAL_AREA = 0.0
    global NP, NE, NPOCH, NOD, NOE, PX, PY
    global CTRL_AREA, TOTAL_AREA

    # EFVM = np.empty([3, EMAX], float)
    # PFVM = np.empty(PMAX, float)
    # BFVM = np.empty(PMAX, float)
    # AFVM = np.empty(PMAX, float)
    # CFVM = np.empty(PMAX, float)
    global EFVM, PFVM, BFVM, AFVM, CFVM

    # CCAJSR = np.empty(PMAX, float)
    # NEWCCA = np.empty(PMAX, float)
    # MEDCCA = np.empty(PMAX, float)
    # RITER = np.empty(PMAX, float)
    # PITER = np.empty(PMAX, float)
    # APK = np.empty(PMAX, float)
    global CCAJSR, NEWCCA, MEDCCA, RITER, PITER, APK

    # DT = 0.0
    # NSTEP = 0.0
    # ILOAD = 0.0
    # RELEASE_TIMES = 0.0
    # DSAVE = 0
    global DT, NSTEP, ILOAD, RELEASE_TIMES
    global DSAVE

    # CCAFSR = 0.0
    # CCAMYO = 0.0
    # KDCSQ = 0.0
    # DCAJSR = 0.0
    # BCSQ = 0.0
    # DCARYR = 0.0
    # DCAFSR = 0.0
    # H_JSR = 0.0
    global KDCSQ, DCAJSR, BCSQ, H_JSR
    global CCAMYO, DCARYR
    global CCAFSR, DCAFSR

    # ICARYR = 0.0
    # ICAFSR = 0.0
    # AVG_CA_JSR = 0.0
    global ICARYR, ICAFSR, AVG_CA_JSR
    # INCLUDE 'T0.INC'
    I = 0
    CCAFSR = 1.0
    CCAMYO = 0.0001
    BCSQ = 14.0
    KDCSQ = 0.63
    H_JSR = 30.0
    DCAJSR = 3.5 * 10 ** 8
    DCARYR = 6.5 * 10 ** 7
    DCAFSR = 0.7854 * 10 ** 6
    DT = 2 * 10 ** -6
    RELEASE_TIMES = 2 * 10 ** -2
    ILOAD = 1
    DSAVE = 100
    NSTEP = 50000
    for I in range(0, NP):
        CCAJSR[I] = 1.0


# *********************************
def DOLOOP_DIFFUSION():
    # INCLUDE 'T0.INC'

    # B_WALL = 1
    # B_INFLOW = 2
    # B_OUTFLOW = 4
    # B_SYMMETRY = 8
    # B_SOURCE = 16
    # PMAX = 50000
    # EMAX = 100000
    # NVEX = 3
    # MAX_NITERATION = 1000
    # UNITEC = 1.610217733
    # MOLNUM = 6.0221367
    global B_WALL, B_INFLOW, B_OUTFLOW, B_SYMMETRY, B_SOURCE, PMAX, EMAX, NVEX, MAX_NITERATION, UNITEC, MOLNUM

    # NP = 0
    # NE = 0
    # NPOCH = np.empty(PMAX, int)
    # NOD = np.empty([NVEX, EMAX], int)
    # NOE = np.empty([NVEX, EMAX], int)
    # PX = np.empty(PMAX, float)
    # PY = np.empty(PMAX, float)
    # CTRL_AREA = np.empty(PMAX, float)
    # TOTAL_AREA = 0.0
    global NP, NE, NPOCH, NOD, NOE, PX, PY
    global CTRL_AREA, TOTAL_AREA

    # EFVM = np.empty([3, EMAX], float)
    # PFVM = np.empty(PMAX, float)
    # BFVM = np.empty(PMAX, float)
    # AFVM = np.empty(PMAX, float)
    # CFVM = np.empty(PMAX, float)
    global EFVM, PFVM, BFVM, AFVM, CFVM

    # CCAJSR = np.empty(PMAX, float)
    # NEWCCA = np.empty(PMAX, float)
    # MEDCCA = np.empty(PMAX, float)
    # RITER = np.empty(PMAX, float)
    # PITER = np.empty(PMAX, float)
    # APK = np.empty(PMAX, float)
    global CCAJSR, NEWCCA, MEDCCA, RITER, PITER, APK

    # DT = 0.0
    # NSTEP = 0.0
    # ILOAD = 0.0
    # RELEASE_TIMES = 0.0
    # DSAVE = 0
    global DT, NSTEP, ILOAD, RELEASE_TIMES
    global DSAVE

    # CCAFSR = 0.0
    # CCAMYO = 0.0
    # KDCSQ = 0.0
    # DCAJSR = 0.0
    # BCSQ = 0.0
    # DCARYR = 0.0
    # DCAFSR = 0.0
    # H_JSR = 0.0
    global KDCSQ, DCAJSR, BCSQ, H_JSR
    global CCAMYO, DCARYR
    global CCAFSR, DCAFSR

    # ICARYR = 0.0
    # ICAFSR = 0.0
    # AVG_CA_JSR = 0.0
    global ICARYR, ICAFSR, AVG_CA_JSR
    # INCLUDE 'T0.INC'
    I = 0
    J = 0
    CURSTEP = 0
    RELEASE_STEP = 0
    FILENAME = ""
    STRN = ""
    CURSTEP = 0
    save = open("DATA\SAVE0000000.dat", "w")
    for I in range(0, NP):
        save.write(str(CCAJSR[I]))
    AVERAGE_CCA()
    CA_CURRENT()
    save.write(str(AVG_CA_JSR))
    save.write(str(ICARYR))
    save.write(str(ICAFSR))
    save.write(str(CURSTEP))
    save.close()
    if ILOAD == 1:
        sav = open("SAVE.DAT", "w+")
        for I in range(0, NP):
            CCAJSR[I] = sav.read(1)
        AVG_CA_JSR = sav.read(1)
        ICARYR = sav.read(1)
        ICAFSR = sav.read(1)
        CURSTEP = sav.read(1)
        sav.close()
    RELEASE_STEP = (RELEASE_TIMES + (10 ** -6)) / DT
    if CURSTEP != RELEASE_STEP:
        DCARYR = 0
        COEFFICIENT()
    for J in range(int(0 if (CURSTEP == '') else CURSTEP), NSTEP):
        PREESTIMATE_EQUATION()
        CORRECTION_EQUATION()
        for I in range(0, NP):
            CCAJSR[I] = NEWCCA[I]
        if J % DSAVE == 0:
            print("STEP =", J)
            STRN = str(J).zfill(8)
            print(STRN, "=", J)
            FILENAME = "DATA\SAVE\\" + STRN + '.dat'
            FIL = open(FILENAME, "w")
            for I in range(0, NP):
                FIL.write(str(CCAJSR[I]))
            AVERAGE_CCA()
            CA_CURRENT()
            FIL.write(str(AVG_CA_JSR))
            FIL.write(str(ICARYR))
            FIL.write(str(ICAFSR))
            FIL.write(str(J))
            FIL.close()
        if J == RELEASE_STEP:
            DCARYR = 0
            COEFFICIENT()
    print("执行成功")


# *************************************************
def PREESTIMATE_EQUATION():
    # INCLUDE 'T0.INC'

    # B_WALL = 1
    # B_INFLOW = 2
    # B_OUTFLOW = 4
    # B_SYMMETRY = 8
    # B_SOURCE = 16
    # PMAX = 50000
    # EMAX = 100000
    # NVEX = 3
    # MAX_NITERATION = 1000
    # UNITEC = 1.610217733
    # MOLNUM = 6.0221367
    global B_WALL, B_INFLOW, B_OUTFLOW, B_SYMMETRY, B_SOURCE, PMAX, EMAX, NVEX, MAX_NITERATION, UNITEC, MOLNUM

    # NP = 0
    # NE = 0
    # NPOCH = np.empty(PMAX, int)
    # NOD = np.empty([NVEX, EMAX], int)
    # NOE = np.empty([NVEX, EMAX], int)
    # PX = np.empty(PMAX, float)
    # PY = np.empty(PMAX, float)
    # CTRL_AREA = np.empty(PMAX, float)
    # TOTAL_AREA = 0.0
    global NP, NE, NPOCH, NOD, NOE, PX, PY
    global CTRL_AREA, TOTAL_AREA

    # EFVM = np.empty([3, EMAX], float)
    # PFVM = np.empty(PMAX, float)
    # BFVM = np.empty(PMAX, float)
    # AFVM = np.empty(PMAX, float)
    # CFVM = np.empty(PMAX, float)
    global EFVM, PFVM, BFVM, AFVM, CFVM

    # CCAJSR = np.empty(PMAX, float)
    # NEWCCA = np.empty(PMAX, float)
    # MEDCCA = np.empty(PMAX, float)
    # RITER = np.empty(PMAX, float)
    # PITER = np.empty(PMAX, float)
    # APK = np.empty(PMAX, float)
    global CCAJSR, NEWCCA, MEDCCA, RITER, PITER, APK

    # DT = 0.0
    # NSTEP = 0.0
    # ILOAD = 0.0
    # RELEASE_TIMES = 0.0
    # DSAVE = 0
    global DT, NSTEP, ILOAD, RELEASE_TIMES
    global DSAVE

    # CCAFSR = 0.0
    # CCAMYO = 0.0
    # KDCSQ = 0.0
    # DCAJSR = 0.0
    # BCSQ = 0.0
    # DCARYR = 0.0
    # DCAFSR = 0.0
    # H_JSR = 0.0
    global KDCSQ, DCAJSR, BCSQ, H_JSR
    global CCAMYO, DCARYR
    global CCAFSR, DCAFSR

    # ICARYR = 0.0
    # ICAFSR = 0.0
    # AVG_CA_JSR = 0.0
    global ICARYR, ICAFSR, AVG_CA_JSR
    # INCLUDE 'T0.INC'
    I = 0
    COEFF = 0.0
    for I in range(0, NP):
        COEFF = CTRL_AREA[I] * (1 + BCSQ * KDCSQ / ((KDCSQ + CCAJSR[I]) ** 2)) / (0.5 * DT * DCAJSR)
        BFVM[I] = COEFF * CCAJSR[I] + CFVM[I]
        AFVM[I] = COEFF + PFVM[I]
        NEWCCA[I] = CCAJSR[I]

    CONJUGATED_GRADIENT_SOLUTION()
    for I in range(0, NP):
        MEDCCA[I] = NEWCCA[I]


# *****************************************************
def CORRECTION_EQUATION():
    # INCLUDE 'T0.INC'

    # B_WALL = 1
    # B_INFLOW = 2
    # B_OUTFLOW = 4
    # B_SYMMETRY = 8
    # B_SOURCE = 16
    # PMAX = 50000
    # EMAX = 100000
    # NVEX = 3
    # MAX_NITERATION = 1000
    # UNITEC = 1.610217733
    # MOLNUM = 6.0221367
    global B_WALL, B_INFLOW, B_OUTFLOW, B_SYMMETRY, B_SOURCE, PMAX, EMAX, NVEX, MAX_NITERATION, UNITEC, MOLNUM

    # NP = 0
    # NE = 0
    # NPOCH = np.empty(PMAX, int)
    # NOD = np.empty([NVEX, EMAX], int)
    # NOE = np.empty([NVEX, EMAX], int)
    # PX = np.empty(PMAX, float)
    # PY = np.empty(PMAX, float)
    # CTRL_AREA = np.empty(PMAX, float)
    # TOTAL_AREA = 0.0
    global NP, NE, NPOCH, NOD, NOE, PX, PY
    global CTRL_AREA, TOTAL_AREA

    # EFVM = np.empty([3, EMAX], float)
    # PFVM = np.empty(PMAX, float)
    # BFVM = np.empty(PMAX, float)
    # AFVM = np.empty(PMAX, float)
    # CFVM = np.empty(PMAX, float)
    global EFVM, PFVM, BFVM, AFVM, CFVM

    # CCAJSR = np.empty(PMAX, float)
    # NEWCCA = np.empty(PMAX, float)
    # MEDCCA = np.empty(PMAX, float)
    # RITER = np.empty(PMAX, float)
    # PITER = np.empty(PMAX, float)
    # APK = np.empty(PMAX, float)
    global CCAJSR, NEWCCA, MEDCCA, RITER, PITER, APK

    # DT = 0.0
    # NSTEP = 0.0
    # ILOAD = 0.0
    # RELEASE_TIMES = 0.0
    # DSAVE = 0
    global DT, NSTEP, ILOAD, RELEASE_TIMES
    global DSAVE

    # CCAFSR = 0.0
    # CCAMYO = 0.0
    # KDCSQ = 0.0
    # DCAJSR = 0.0
    # BCSQ = 0.0
    # DCARYR = 0.0
    # DCAFSR = 0.0
    # H_JSR = 0.0
    global KDCSQ, DCAJSR, BCSQ, H_JSR
    global CCAMYO, DCARYR
    global CCAFSR, DCAFSR

    # ICARYR = 0.0
    # ICAFSR = 0.0
    # AVG_CA_JSR = 0.0
    global ICARYR, ICAFSR, AVG_CA_JSR
    # INCLUDE 'T0.INC'
    I = 0
    N1 = 0
    N2 = 0
    N3 = 0
    COEFF = 0.0
    for I in range(0, NP):
        COEFF = CTRL_AREA[I] * (1 + BCSQ * KDCSQ / ((KDCSQ + MEDCCA[I]) ** 2)) / (0.5 * DT * DCAJSR)
        BFVM[I] = (COEFF - PFVM[I]) * CCAJSR[I] + CFVM[I] + CFVM[I]
        AFVM[I] = COEFF + PFVM[I]
    for I in range(0, NE):
        N1 = NOD[0, I]
        N2 = NOD[1, I]
        N3 = NOD[2, I]
        BFVM[N1] = BFVM[N1] - EFVM[0, I] * CCAJSR[N2] - EFVM[2, I] * CCAJSR[N3]
        BFVM[N2] = BFVM[N2] - EFVM[0, I] * CCAJSR[N1] - EFVM[1, I] * CCAJSR[N3]
        BFVM[N3] = BFVM[N3] - EFVM[2, I] * CCAJSR[N1] - EFVM[1, I] * CCAJSR[N2]
    CONJUGATED_GRADIENT_SOLUTION()


# *****************************************
def CONJUGATED_GRADIENT_SOLUTION():
    # INCLUDE 'T0.INC'

    # B_WALL = 1
    # B_INFLOW = 2
    # B_OUTFLOW = 4
    # B_SYMMETRY = 8
    # B_SOURCE = 16
    # PMAX = 50000
    # EMAX = 100000
    # NVEX = 3
    # MAX_NITERATION = 1000
    # UNITEC = 1.610217733
    # MOLNUM = 6.0221367
    global B_WALL, B_INFLOW, B_OUTFLOW, B_SYMMETRY, B_SOURCE, PMAX, EMAX, NVEX, MAX_NITERATION, UNITEC, MOLNUM

    # NP = 0
    # NE = 0
    # NPOCH = np.empty(PMAX, int)
    # NOD = np.empty([NVEX, EMAX], int)
    # NOE = np.empty([NVEX, EMAX], int)
    # PX = np.empty(PMAX, float)
    # PY = np.empty(PMAX, float)
    # CTRL_AREA = np.empty(PMAX, float)
    # TOTAL_AREA = 0.0
    global NP, NE, NPOCH, NOD, NOE, PX, PY
    global CTRL_AREA, TOTAL_AREA

    # EFVM = np.empty([3, EMAX], float)
    # PFVM = np.empty(PMAX, float)
    # BFVM = np.empty(PMAX, float)
    # AFVM = np.empty(PMAX, float)
    # CFVM = np.empty(PMAX, float)
    global EFVM, PFVM, BFVM, AFVM, CFVM

    # CCAJSR = np.empty(PMAX, float)
    # NEWCCA = np.empty(PMAX, float)
    # MEDCCA = np.empty(PMAX, float)
    # RITER = np.empty(PMAX, float)
    # PITER = np.empty(PMAX, float)
    # APK = np.empty(PMAX, float)
    global CCAJSR, NEWCCA, MEDCCA, RITER, PITER, APK

    # DT = 0.0
    # NSTEP = 0.0
    # ILOAD = 0.0
    # RELEASE_TIMES = 0.0
    # DSAVE = 0
    global DT, NSTEP, ILOAD, RELEASE_TIMES
    global DSAVE

    # CCAFSR = 0.0
    # CCAMYO = 0.0
    # KDCSQ = 0.0
    # DCAJSR = 0.0
    # BCSQ = 0.0
    # DCARYR = 0.0
    # DCAFSR = 0.0
    # H_JSR = 0.0
    global KDCSQ, DCAJSR, BCSQ, H_JSR
    global CCAMYO, DCARYR
    global CCAFSR, DCAFSR

    # ICARYR = 0.0
    # ICAFSR = 0.0
    # AVG_CA_JSR = 0.0
    global ICARYR, ICAFSR, AVG_CA_JSR
    # INCLUDE 'T0.INC'
    N = 0
    I = 0
    N1 = 0
    N2 = 0
    N3 = 0
    QUP = 0.0
    QDOWN = 0.0
    QK = 0.0
    EUP = 0.0
    EDOWN = 0.0
    EK = 0.0
    MAX_ERROR = 0.0
    P_ERROR = 0.0
    for I in range(0, NP):
        RITER[I] = BFVM[I] - AFVM[I] * NEWCCA[I]

    for I in range(0, NE):
        N1 = NOD[0, I]
        N2 = NOD[1, I]
        N3 = NOD[2, I]
        RITER[N1] = RITER[N1] - EFVM[0, I] * NEWCCA[N2] - EFVM[2, I] * NEWCCA[N3]
        RITER[N2] = RITER[N2] - EFVM[0, I] * NEWCCA[N1] - EFVM[1, I] * NEWCCA[N3]
        RITER[N3] = RITER[N3] - EFVM[2, I] * NEWCCA[N1] - EFVM[1, I] * NEWCCA[N2]

    for I in range(0, NP):
        PITER[I] = RITER[I]
    EUP = 0.0
    for I in range(0, NP):
        EUP = EUP + RITER[I] * RITER[I]
    for N in range(0, MAX_NITERATION):
        for I in range(0, NP):
            APK[I] = AFVM[I] * PITER[I]
        for I in range(0, NE):
            N1 = NOD[0, I]
            N2 = NOD[1, I]
            N3 = NOD[2, I]
            APK[N1] = APK[N1] + EFVM[0, I] * PITER[N2] + EFVM[2, I] * PITER[N3]
            APK[N2] = APK[N2] + EFVM[0, I] * PITER[N1] + EFVM[1, I] * PITER[N3]
            APK[N3] = APK[N3] + EFVM[2, I] * PITER[N1] + EFVM[1, I] * PITER[N2]
        QUP = EUP
        QDOWN = 0.0
        for I in range(0, NP):
            QDOWN = QDOWN + APK[I] * PITER[I]
        if QDOWN > 0:
            QK = QUP / QDOWN
        for I in range(0, NP):
            NEWCCA[I] = NEWCCA[I] + QK * PITER[I]
            RITER[I] = RITER[I] - QK * APK[I]

        MAX_ERROR = 0.0
        for I in range(0, NP):
            P_ERROR = abs(QK * PITER[I] / NEWCCA[I])
            if MAX_ERROR < P_ERROR:
                MAX_ERROR = P_ERROR
        if MAX_ERROR < 10**-5 and N >= 50:
            continue

        EUP = 0.0
        for I in range(0, NP):
            EUP = EUP + RITER[I] * RITER[I]
        EDOWN = QDOWN
        if EDOWN > 0:
            EK = EUP / EDOWN

        for I in range(0, NP):
            PITER[I] = RITER[I] + EK * PITER[I]


# ********************************************************
def COEFFICIENT():
    #  INCLUDE 'T0.INC'

    # B_WALL = 1
    # B_INFLOW = 2
    # B_OUTFLOW = 4
    # B_SYMMETRY = 8
    # B_SOURCE = 16
    # PMAX = 50000
    # EMAX = 100000
    # NVEX = 3
    # MAX_NITERATION = 1000
    # UNITEC = 1.610217733
    # MOLNUM = 6.0221367
    global B_WALL, B_INFLOW, B_OUTFLOW, B_SYMMETRY, B_SOURCE, PMAX, EMAX, NVEX, MAX_NITERATION, UNITEC, MOLNUM

    # NP = 0
    # NE = 0
    # NPOCH = np.empty(PMAX, int)
    # NOD = np.empty([NVEX, EMAX], int)
    # NOE = np.empty([NVEX, EMAX], int)
    # PX = np.empty(PMAX, float)
    # PY = np.empty(PMAX, float)
    # CTRL_AREA = np.empty(PMAX, float)
    # TOTAL_AREA = 0.0
    global NP, NE, NPOCH, NOD, NOE, PX, PY
    global CTRL_AREA, TOTAL_AREA

    # EFVM = np.empty([3, EMAX], float)
    # PFVM = np.empty(PMAX, float)
    # BFVM = np.empty(PMAX, float)
    # AFVM = np.empty(PMAX, float)
    # CFVM = np.empty(PMAX, float)
    global EFVM, PFVM, BFVM, AFVM, CFVM

    # CCAJSR = np.empty(PMAX, float)
    # NEWCCA = np.empty(PMAX, float)
    # MEDCCA = np.empty(PMAX, float)
    # RITER = np.empty(PMAX, float)
    # PITER = np.empty(PMAX, float)
    # APK = np.empty(PMAX, float)
    global CCAJSR, NEWCCA, MEDCCA, RITER, PITER, APK

    # DT = 0.0
    # NSTEP = 0.0
    # ILOAD = 0.0
    # RELEASE_TIMES = 0.0
    # DSAVE = 0
    global DT, NSTEP, ILOAD, RELEASE_TIMES
    global DSAVE

    # CCAFSR = 0.0
    # CCAMYO = 0.0
    # KDCSQ = 0.0
    # DCAJSR = 0.0
    # BCSQ = 0.0
    # DCARYR = 0.0
    # DCAFSR = 0.0
    # H_JSR = 0.0
    global KDCSQ, DCAJSR, BCSQ, H_JSR
    global CCAMYO, DCARYR
    global CCAFSR, DCAFSR

    # ICARYR = 0.0
    # ICAFSR = 0.0
    # AVG_CA_JSR = 0.0
    global ICARYR, ICAFSR, AVG_CA_JSR
    #  INCLUDE 'T0.INC'

    E = 0
    I = 0
    J = 0
    K = 0
    N1 = 0
    N2 = 0
    N3 = 0
    VOL6 = 0.0
    VOL = 0.0
    TOTAL_VOL = 0.0
    MATRIX0 = np.empty([3, 3], float)
    MATRIX1 = np.empty([3, 3], float)
    MATRIX2 = np.empty([3, 3], float)
    MATRIX4 = np.empty([2, 2], float)
    VER1 = np.empty(2, float)
    VER2 = np.empty(2, float)
    BE = np.empty(3, float)
    CE = np.empty(3, float)
    LENGTH = 0.0
    TOTAL_VOL = 0.0
    for I in range(0, NP):
        PFVM[I] = 0.0
        AFVM[I] = 0.0
        BFVM[I] = 0.0
        CFVM[I] = 0.0
        CTRL_AREA[I] = 0
    for E in range(0, NE):
        N1 = NOD[0, E]
        N2 = NOD[1, E]
        N3 = NOD[2, E]
        for I in range(0, 3):
            MATRIX1[I, 0] = 1.0
            MATRIX1[I, 1] = PX[NOD[I, E]]
            MATRIX1[I, 2] = PY[NOD[I, E]]
        for I in range(0, 3):
            for J in range(0, 3):
                MATRIX0[I, J] = MATRIX1[I, J]
        DET(MATRIX1, 3, VOL6)
        VOL = VOL6 / 2.0
        TOTAL_VOL = TOTAL_VOL + VOL

        for I in range(0, 3):
            CTRL_AREA[NOD[I, E]] = CTRL_AREA[NOD[I, E]] + VOL

        for I in range(0, 3):
            for J in range(0, 3):
                for K in range(0, 3):
                    MATRIX2[J, K] = MATRIX0[J, K]
            for J in range(1, 3):
                MATRIX2[I, J] = MATRIX0[2, J]
            for J in range(0, 2):
                MATRIX2[J, 0] = MATRIX2[J, 1] - PX[NOD[I, E]]
                MATRIX2[J, 1] = MATRIX2[J, 2] - PY[NOD[I, E]]
            for J in range(0, 2):
                VER1[J] = -1.0
            for J in range(0, 2):
                for K in range(0, 2):
                    MATRIX4[J, K] = MATRIX2[J, K + 1]
            AXEQB(MATRIX4, VER1, 2, VER2)
            BE[I] = VER2[0]
            CE[I] = VER2[1]
        #  A(N1,N2) = A(N2, N1)
        EFVM[0, E] = (CE[1] * (PX[N3] - PX[N2]) - BE[1] * (PY[N3] - PY[N2]) + CE[0] * (PX[N1] - PX[N3]) - BE[0] * (
                PY[N1] - PY[N3])) / 2.0
        #  A(N2,N3) = A(N3, N2)
        EFVM[1, E] = (CE[1] * (PX[N2] - PX[N1]) - BE[1] * (PY[N2] - PY[N1]) + CE[2] * (PX[N1] - PX[N3]) - BE[2] * (
                PY[N1] - PY[N3])) / 2.0
        #  A(N3,N1) = A(N1, N3)
        EFVM[2, E] = (CE[2] * (PX[N3] - PX[N2]) - BE[2] * (PY[N3] - PY[N2]) + CE[0] * (PX[N2] - PX[N1]) - BE[0] * (
                PY[N2] - PY[N1])) / 2.0
        PFVM[N1] = PFVM[N1] + CE[0] * (PX[N3] - PX[N2]) - BE[0] * (PY[N3] - PY[N2])
        PFVM[N2] = PFVM[N2] + CE[1] * (PX[N1] - PX[N3]) - BE[1] * (PY[N1] - PY[N3])
        PFVM[N3] = PFVM[N3] + CE[2] * (PX[N2] - PX[N1]) - BE[2] * (PY[N2] - PY[N1])
        # *** OUTFLOW
        if NPOCH[N2] == B_OUTFLOW and NPOCH[N3] == B_OUTFLOW:
            LENGTH = sqrt((PY[N3] - PY[N2]) ** 2 + (PX[N3] - PX[N2]) ** 2)
        PFVM[N1] = PFVM[N1] + DCARYR * LENGTH / DCAJSR
        PFVM[N2] = PFVM[N2] + DCARYR * LENGTH / DCAJSR
        PFVM[N3] = PFVM[N3] + DCARYR * LENGTH / DCAJSR
        if NPOCH[N1] == B_OUTFLOW and NPOCH[N3] == B_OUTFLOW:
            LENGTH = sqrt((PY[N3] - PY[N2]) ** 2 + (PX[N3] - PX[N2]) ** 2)
        PFVM[N1] = PFVM[N1] + DCARYR * LENGTH / DCAJSR
        PFVM[N2] = PFVM[N2] + DCARYR * LENGTH / DCAJSR
        PFVM[N3] = PFVM[N3] + DCARYR * LENGTH / DCAJSR
        if NPOCH[N2] == B_OUTFLOW and NPOCH[N1] == B_OUTFLOW:
            LENGTH = sqrt((PY[N1] - PY[N2]) ** 2 + (PX[N1] - PX[N2]) ** 2)
        PFVM[N3] = PFVM[N3] + DCARYR * LENGTH / DCAJSR
        PFVM[N2] = PFVM[N2] + DCARYR * LENGTH / DCAJSR
        PFVM[N1] = PFVM[N1] + DCARYR * LENGTH / DCAJSR
        #  INFLOW
        if NPOCH[N2] == B_INFLOW and NPOCH[N3] == B_INFLOW:
            LENGTH = sqrt((PY[N3] - PY[N2]) ** 2 + (PX[N3] - PX[N2]) ** 2)
        PFVM[N1] = PFVM[N1] + DCAFSR * LENGTH / DCAJSR
        PFVM[N2] = PFVM[N2] + DCAFSR * LENGTH / DCAJSR
        PFVM[N3] = PFVM[N3] + DCAFSR * LENGTH / DCAJSR
        CFVM[N1] = CFVM[N1] + CCAFSR * DCAFSR * LENGTH / DCAJSR
        CFVM[N2] = CFVM[N2] + CCAFSR * DCAFSR * LENGTH / DCAJSR
        CFVM[N3] = CFVM[N3] + CCAFSR * DCAFSR * LENGTH / DCAJSR
        if NPOCH[N1] == B_INFLOW and NPOCH[N3] == B_INFLOW:
            LENGTH = sqrt((PY[N3] - PY[N1]) ** 2 + (PX[N3] - PX[N1]) ** 2)
        PFVM[N1] = PFVM[N1] + DCAFSR * LENGTH / DCAJSR
        PFVM[N2] = PFVM[N2] + DCAFSR * LENGTH / DCAJSR
        PFVM[N3] = PFVM[N3] + DCAFSR * LENGTH / DCAJSR
        CFVM[N1] = CFVM[N1] + CCAFSR * DCAFSR * LENGTH / DCAJSR
        CFVM[N2] = CFVM[N2] + CCAFSR * DCAFSR * LENGTH / DCAJSR
        CFVM[N3] = CFVM[N3] + CCAFSR * DCAFSR * LENGTH / DCAJSR
        if NPOCH[N2] == B_INFLOW and NPOCH[N1] == B_INFLOW:
            LENGTH = sqrt((PY[N1] - PY[N2]) ** 2 + (PX[N1] - PX[N2]) ** 2)
        PFVM[N1] = PFVM[N1] + DCAFSR * LENGTH / DCAJSR
        PFVM[N2] = PFVM[N2] + DCAFSR * LENGTH / DCAJSR
        PFVM[N3] = PFVM[N3] + DCAFSR * LENGTH / DCAJSR
        CFVM[N1] = CFVM[N1] + CCAFSR * DCAFSR * LENGTH / DCAJSR
        CFVM[N2] = CFVM[N2] + CCAFSR * DCAFSR * LENGTH / DCAJSR
        CFVM[N3] = CFVM[N3] + CCAFSR * DCAFSR * LENGTH / DCAJSR
        TOTAL_AREA = TOTAL_VOL * 3
        # **************************************************


def LOAD_GRIDINFO():
    # INCLUDE 'T0.INC'

    # B_WALL = 1
    # B_INFLOW = 2
    # B_OUTFLOW = 4
    # B_SYMMETRY = 8
    # B_SOURCE = 16
    # PMAX = 50000
    # EMAX = 100000
    # NVEX = 3
    # MAX_NITERATION = 1000
    # UNITEC = 1.610217733
    # MOLNUM = 6.0221367
    global B_WALL, B_INFLOW, B_OUTFLOW, B_SYMMETRY, B_SOURCE, PMAX, EMAX, NVEX, MAX_NITERATION, UNITEC, MOLNUM

    # NP = 0
    # NE = 0
    # NPOCH = np.empty(PMAX, int)
    # NOD = np.empty([NVEX, EMAX], int)
    # NOE = np.empty([NVEX, EMAX], int)
    # PX = np.empty(PMAX, float)
    # PY = np.empty(PMAX, float)
    # CTRL_AREA = np.empty(PMAX, float)
    # TOTAL_AREA = 0.0
    global NP, NE, NPOCH, NOD, NOE, PX, PY
    global CTRL_AREA, TOTAL_AREA

    # EFVM = np.empty([3, EMAX], float)
    # PFVM = np.empty(PMAX, float)
    # BFVM = np.empty(PMAX, float)
    # AFVM = np.empty(PMAX, float)
    # CFVM = np.empty(PMAX, float)
    global EFVM, PFVM, BFVM, AFVM, CFVM

    # CCAJSR = np.empty(PMAX, float)
    # NEWCCA = np.empty(PMAX, float)
    # MEDCCA = np.empty(PMAX, float)
    # RITER = np.empty(PMAX, float)
    # PITER = np.empty(PMAX, float)
    # APK = np.empty(PMAX, float)
    global CCAJSR, NEWCCA, MEDCCA, RITER, PITER, APK

    # DT = 0.0
    # NSTEP = 0.0
    # ILOAD = 0.0
    # RELEASE_TIMES = 0.0
    # DSAVE = 0
    global DT, NSTEP, ILOAD, RELEASE_TIMES
    global DSAVE

    # CCAFSR = 0.0
    # CCAMYO = 0.0
    # KDCSQ = 0.0
    # DCAJSR = 0.0
    # BCSQ = 0.0
    # DCARYR = 0.0
    # DCAFSR = 0.0
    # H_JSR = 0.0
    global KDCSQ, DCAJSR, BCSQ, H_JSR
    global CCAMYO, DCARYR
    global CCAFSR, DCAFSR

    # ICARYR = 0.0
    # ICAFSR = 0.0
    # AVG_CA_JSR = 0.0
    global ICARYR, ICAFSR, AVG_CA_JSR, OLDCCA
    # INCLUDE 'T0.INC'
    I = 0
    GRI = open('gridt.dat', "r")
    NP = GRI.read(1)
    # NP_INT = int.from_bytes(NP, byteorder='little', signed=True)
    for I in range(0, NP):
        PX[I], PY[I] = GRI.read(2)
    GRI.close()
    NPO = open("npoch.dat", "rb+")
    NPO1 = NPO.read(1)
    # NPO1_INT = int.from_bytes(NPO1, byteorder='little', signed=True)
    for I in range(0, NP):
        NPOCH[I] = int.from_bytes(NPO.read(1), byteorder='little', signed=True)
    NPO.close()
    NO1 = open("nod.dat", "rb+")
    NE = NO1.read(1)
    # NE_INT = int.from_bytes(NP, byteorder='little', signed=True)
    for I in range(0, NE):
        NOD[0, I], NOD[1, I], NOD[2, I] = NO1.read(3)
    NO1.close()
    NO2 = open("noe.dat", "rb+")
    for i in range(0, NE):
        NOE[0, I], NOE[1, I], NOE[2, I] = NO2.read(3)
    NO2.close()


# *******************************************************
def DET(MATRI, NUM, DET_MATRI):
    #NUM = 0
    I = 0
    J = 0
    K = 0
    SIGN_1 = 0
    DET_MATRI = 0.0
    DET_MATRIX = 0.0
    REAL_1 = 0.0
    REAL_2 = 0.0
    MATRI = np.empty([NUM, NUM], float)
    MATRIX = np.empty([NUM, NUM], float)

    for I in range(0, NUM):
        for J in range(0, NUM):
            MATRIX[I, J] = MATRI[I, J]
    DET_MATRIX = 1
    SIGN_1 = 1
    for I in range(0, NUM-1):
        REAL_1 = MATRIX[I, I]
        for J in range(I, NUM):
            if abs(MATRIX[J, I]) > abs(REAL_1):
                for K in range(I, NUM):
                    REAL_1 = MATRIX[I, K]
                    MATRIX[I, K] = MATRIX[J, K]
                    MATRIX[J, K] = REAL_1
                SIGN_1 = SIGN_1 * (-1)
            REAL_1 = MATRIX[I, I]
        REAL_1 = MATRIX[I, I]
        if abs(REAL_1) < 10 ** (-8):
            DET_MATRI = 0.0
            return
        MATRIX[I, I] = 1.0
        DET_MATRIX = DET_MATRIX * REAL_1
        for J in range(I+1, NUM):
            REAL_2 = MATRIX[J, I] / REAL_1
            MATRIX[J, I] = 0.0
            for K in range(I+1, NUM):
                MATRIX[J, K] = MATRIX[J, K] - REAL_2 * MATRIX[I, K]
    DET_MATRIX = DET_MATRIX * MATRIX[NUM, NUM] * SIGN_1

    DET_MATRI = DET_MATRIX


# ***********************************************
def AXEQB(ARR1, VERB1, NUM, VERX1):
    NUM = 0
    ARR1 = np.empty([NUM, NUM], float)
    ARR = np.empty([NUM, NUM], float)
    VERB1 = np.empty(NUM, float)
    VERX1 = np.empty(NUM, float)
    VERB = np.empty(NUM, float)
    VERX = np.empty(NUM, float)
    I = 0
    J = 0
    K = 0
    REAL_1 = 0.0
    REAL_2 = 0.0
    for I in range(0, NUM):
        for J in range(0, NUM):
            ARR[I, J] = ARR1[I, J]
        VERB[I] = VERB1[I]
    for I in range(0, NUM-1):
        REAL_1 = ARR[I, I]
        for J in range(I+1, NUM):
            if abs(ARR[J, I]) > abs(REAL_1):
                for K in range(I, NUM):
                    REAL_1 = ARR[I, K]
                    ARR[I, K] = ARR[J, K]
                    ARR[J, K] = REAL_1
                REAL_1 = VERB[I]
                VERB[I] = VERB[J]
                VERB[J] = REAL_1
            REAL_1 = ARR[I, I]
        REAL_1 = ARR[I, I]
        ARR[I, I] = 1.0
        if abs(REAL_1) < (10 ** -8):
            print("DET(ARR)=0,THIS EQUATION NO ANSWER")
            print(ARR1)
            return
        for J in range(I + 1, NUM):
            ARR[I, J] = ARR[I, J] / REAL_1
        VERB[I] = VERB[I] / REAL_1
        for J in range(I + 1, NUM):
            REAL_2 = ARR[J, I]
            ARR[J, I] = 0.0
            for K in range(I + 1, NUM):
                ARR[J, K] = ARR[J, K] - REAL_2 * ARR[I, K]
            VERB[J] = VERB[J] - REAL_2 * VERB[I]

        if abs(ARR[NUM, NUM]) < 10 ** -8:
            print("DET(ARR)=0,THIS EQUATION NO ANSWER")
            print(ARR1)
            return
        VERX[NUM] = VERB[NUM] / ARR[NUM, NUM]
        for I in range(NUM - 2, 1, -1):
            VERX[I] = VERB[I]
            for J in range(NUM, I, -1):
                VERX[I] = VERX[I] - ARR[I, J] * VERX[J]
        for I in range(0, NUM):
            VERX1[I] = VERX[I]


# ********************************************
if __name__ == '__main__':
    MAIN()
