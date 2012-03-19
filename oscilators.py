from numpy import *

# funkcja liczy zwyczajna srednia artmetyczna z podanej jej tablicy, przekazywac tablice jednowymiarowa!
def simpleArthmeticAverage(array):
	result = 0
	for i in range(array.size):
		result += array[i]
	result /= array.size
	return result

# liczy srednia wazona gdzie najmniejsza wage = 1 ma pierwszy element, najwieksza wage element ostatni z waga rowna dlugosci tablicy
def weightedAverage(array):
	result = 0
	tableSum = arange(1,array.size+1,1)
	divisor = tableSum.sum()
	for i in range(array.size):
		result += array[i]*(i+1)
	result /= divisor
	return result

# liczy srednia expotencjalna gdzie alfa = 2/(1+N)
# Najwiekszy 'potencjal' ma wartosc ostatnia, pierwsza wartosc ma potencjal (1-alfa)^N
def expotentialAverage(array):
	result = 0
	divisor = 0
	factor = 2.0/(array.size+1)
	for i in range(array.size):
		result += array[i]*((1-factor)**(array.size-i-1))
		divisor += (1-factor)**(array.size-i-1)
	result /= divisor
	return result

# Indeks new High/new Low. Zwraca pojedyncza wartosc, przekazujemy zazwyczaj tablice zamkniec gieldy.
def highLowIndex(array):
	size = array.size
	highest = array[0]
	lowest = array[0]
	numberOfHighest = 1.0
	numberOfLowest = 1.0
	for i in range(1,size):
		if array[i] > highest:
			highest = array[i]
			numberOfHighest += 1.0
		if array[i] < lowest:
			lowest = array[i]
			numberOfLowest += 1.0
	return (numberOfHighest/(numberOfHighest+numberOfLowest))*100

# Standardowe odchylenie dla tablicy array, koniecznie jednowymiarowa
def standardDeviation(array):
	size = array.size
	average = simpleArthmeticAverage(array)
	total = 0
	for i in range(0,size):
		total += (array[i] - average)**2
	total /= size
	total = math.sqrt(total)
	return total

# Oblicza tablice wartosci Wsteg Bollingera :
# array - wartosci gieldowe(najlepiej kolejne zamkniecia gield)
# duration - okres obliczanego wskaznika, WAZNE ABY array BYLA 2x WIEKSZA NIZ duration (patrz movingAverage)
# mode - 1: Gorna wstega Bollingera, 2: Dolna wstega Bollingera
# D - stala uzywana do odchylania wsteg, domyslnie 2
def bollingerBands(array,duration,mode,D):
	values = zeros(array.size/2)
	size = array.size
	j = 0
	for i in range(size/2,size):
		tempTable = array[i-duration+1:i+1]
		if mode == 1:
			values[j] = simpleArthmeticAverage(tempTable)+(D*standardDeviation(tempTable))
		if mode == 2:
			values[j] = simpleArthmeticAverage(tempTable)-(D*standardDeviation(tempTable))
		j += 1
	return values

# array - tablica z wartosciami cen zamkniec itp, duration - czas trwania liczonej sredniej krokowej
# Zwraca tablice jednowymiarowa z wartosciami sredniej krokowej dla przedzialu [size/2,size-1], aby obliczyc wartosci tablica wejsciowa musi byc 2x wieksza od zakresu(duration)
# modes : 1-SMA(simple moving average), 2-WMA(weighted moving average), 3-EMA(expotential moving average) 
def movingAverage(array,duration,mode):
        values = zeros(array.size/2)
        size = array.size
        j = 0
        for i in range(size/2,size):
                tempTable = array[i-duration+1:i+1]
                if mode == 1:
                        values[j] = simpleArthmeticAverage(tempTable)
                if mode == 2:
                        values[j] = weightedAverage(tempTable)
                if mode == 3:
                        values[j] = expotentialAverage(tempTable)
                j += 1
        return values

# Zwraca tablice wartosci wskaznika Impetu(Momentum) dla danej tablicy. Co wazne, ilosc obliczonych wartosci to rozmiar tablicy - duration
def momentum(array,duration):
	values = zeros(array.size-duration)
	size = array.size
	j = 0
	for i in range(duration,size):
		values[j] = array[i] - array[i-duration]
		j += 1
	return values

# Jak wyzej
def ROC(array, duration):
	values = zeros(array.size-duration)
	size = array.size
	j = 0
	for i in range(duration,size):
		values[j] = ((array[i] - array[i-duration])/(array[i-duration]))*100
		j += 1
	return values

# Srednie odchylenie tablicy
def meanDeviation(array):
	result = 0
	average = simpleArthmeticAverage(array)
	for i in range(0,array.size):
		temp = array[i] - average
		if temp<0:
			temp = -1*temp
		result += temp
	result /= array.size
	return result

# Funkcja zwraca tablice z wartosciami wskaznika Comodity Index Channel, dlugosc tablicy jest rowna
# closeTable.size-duration
def CCI(closeTable,lowTable,highTable,duration):
	size = closeTable.size
	typicalPricesTable = zeros(size)
	for i in range(0,size):
		typicalPricesTable[i] = (closeTable[i]+lowTable[i]+highTable[i])/3
	values = zeros(size-duration+1)
	j = 0
	for i in range(duration-1,size):
		tempTypical = typicalPricesTable[i-duration+1:i+1]
		average = simpleArthmeticAverage(tempTypical)
		deviation = meanDeviation(tempTypical)
		values[j] = (typicalPricesTable[i] - average)/(0.015*deviation)
		j += 1
	return values

# Korzysta z niej RSI, sumuje elementy tablicy i w zaleznosci od mode, zmienia znak lub nie :)
def sumUnderCondition(array,mode):
        result = 0
        size = array.size
        if mode == 1:
                for i in range(0,size):
                        if array[i] >= 0:
                                result += array[i]
        if mode == 2:
                for i in range(0,size):
                        if array[i] <= 0:
                                result += array[i]
                result *= -1
        return result

# Liczy wskaznik RSI, przekazujemy wartosci najlepiej zamkniec sesji, otrzymujemy tablice
# wielkosci array-duration ze wartosciami RSI dla indeksow tablicy [duration,size]
def RSI(array, duration):
        size = array.size
        values = zeros(size-duration)
        gainLossTable = zeros(size)
        for i in range(1,size):
                gainLossTable[i-1] = array[i]-array[i-1]
        k = 0
        averageGain = (sumUnderCondition(gainLossTable[0:duration-1],1))/duration
        averageLoss = (sumUnderCondition(gainLossTable[0:duration-1],2))/duration
        for j in range(duration,size):    
                RS = averageGain/averageLoss
                RSI = 100.0 - (100.0/(1+RS))
                values[k] = RSI
                k += 1
                if j < size:
                        if gainLossTable[j] > 0:
                                averageGain = (averageGain*13 + gainLossTable[j])/duration
                                averageLoss = (averageLoss*13 + 0)/duration
                        if gainLossTable[j] <= 0:
                                averageGain = (averageGain*13 + 0)/duration
                                averageLoss = (averageLoss*13 + (-1)*gainLossTable[j])/duration
        return values

# Zwraca najwiekszy element tablicy
def highest(array):
        max = array[0]
        for i in range(0,array.size):
                if array[i] > max:
                        max = array[i]
        return max

# Zwraca najmniejszy element tablicy
def lowest(array):
        min = array[0]
        for i in range(0,array.size):
                if array[i] < min:
                        min = array[i]
        return min

# Inaczej zwany oscylator %R Wazne aby przekazywac tablice tej samej dlugosci
# Zwraca tablice wielkosci size-duration z wartosciami oscylatora %R
def williamsOscilator(highTable,lowTable,closeTable,duration):
        size = highTable.size
        values = zeros(size-duration)
        j = 0
        for i in range(duration-1,size-1):
                lowestValue = lowest(lowTable[i-duration+1:i+1])
                highestValue = highest(highTable[i-duration+1:i+1])
                values[j] = ((highestValue - closeTable[i])/(highestValue - lowestValue))*(-100.0)
                j += 1
        return values
def testR1():
        high = array([2.11,2.15,2.22,2.28,2.30])
        low = array([2.00,2.08,2.10,2.15,2.20])
        open = array([2.05,2.10,2.15,2.20,2.25])
        return williamsOscilator(high,low,open,1)

def testR():
        high = array([127.01,127.62,126.59,127.35,128.17,128.43,127.37,126.42,126.9,126.85,125.65,125.72,127.16,127.72,127.69,128.22,128.27,127.74,128.77,129.29,130.06,129.12,129.29,128.47,128.09,128.65,129.14,128.64])
        low = array([125.36,126.16,124.93,126.09,126.82,126.48,126.03,124.83,126.39,125.72,124.56,124.57,125.07,126.86,126.63,126.8,126.13,125.92,126.99,127.81,128.47,128.06,127.61,127.6,127.0,126.9,127.49,127.4])
        close = array([1,1,1,1,1,1,1,1,1,1,1,1,1,127.29,127.18,128.01,127.11,127.73,127.06,127.33,128.71,127.87,128.58,128.6,127.93,128.11,127.6,127.6,128.69,128.27])
        return williamsOscilator(high,low,close, 14) 

# Nalezy przekazac tablice ilosci spadajacych i wzrastajacych spolek.
# Kazdy indeks odpowiada jednemu dniu. 
def adLine(advances, declines):
        size = advances.size
        values = zeros(size)
        for i in range(0,size):
                netAdvance = advances[i]-declines[i]
                if i==0:
                        values[i] = netAdvance
                else:
                        values[i] = values[i-1] + netAdvance
        return values

# Minimalne przekazane tablice musza miec conajmmniej 40 wartosci.
# Wersja nieprzetestowana
def mcClellanOscillator(advances,declines):
        size = advances.size
        values = zeros(size)
        ratioAdjusted = zeros(size)
        for i in range(0,size):
                ratioAdjusted[i] = advances[i]-declines[i]
        result19 = movingAverage(ratioAdjusted,19,3)
        result39 = movingAverage(ratioAdjusted,39,3)
        return result19-result39
