import math


def media_cu_teza():
	print('Scrie notele fara teza, cu spatii intre ele.')
	note = [int(i) for i in raw_input('Notele: ').split(' ')]  # Din cate stiu eu, magie neagra.
	nota_teza = int(raw_input('Scrie nota la teza: '))  # aparent raw_input le face str oricum
	suma_note = sum(note)
	media_note = suma_note / len(note)
	rezultat = (3 * media_note + nota_teza) / 4
	return 'Media este ' + str(int(round(rezultat)))


def media_fara_teza():
	print('Scrie notele, cu spatii intre ele.')
	note = [int(i) for i in raw_input('Notele: ').split(' ')]
	rezultat = sum(note) / len(note)
	return 'Media este ' + str(int(round(rezultat)))


def gol_de_note():  # asta intreaba ce medie vrei si spune de ce note ai nevoie
	print('Ce note ai deocamdata?')
	note_0 = [int(i) for i in raw_input('Scrie cu un spatiu intre ele: ').split(' ')]  # am devenit expert deja
	medie_vruta = int(raw_input('Ce medie  minima ai vrea sa ai? '))
	nr_note_trebuite = int(raw_input('In cate note trebuie sa atingi aceasta medie? '))
	nr_note_total = len(note_0) + nr_note_trebuite
	suma_note_trebuite = math.ceil(nr_note_total * (medie_vruta - 0.5) - sum(note_0))  # idk daca e buna
	print('Suma notelor pe care trebuie sa le iei este ' + str(suma_note_trebuite) + '.')


def re_salut():
	alegere = raw_input('Mai vreti sa faceti altceva?(scrieti d sau n): ')  # input() e ciudat
	if str(alegere) == 'd':
		return salut()
	else:
		return 'OK'


def salut():
	print ' 1. Vreau media unei materii cu teza.'
	print ' 2. Vreau media unei materii fara teza.'
	print ' 3. Vreau sa stiu ce note trebuie sa iau ca sa ajung la o anumita medie'
	raspuns = raw_input('Scrie numarul care corespunde cu ce ai vrea sa faci: ')
	if raspuns == '1':
		print(media_cu_teza())
		print(re_salut())
	elif raspuns == '2':
		print(media_fara_teza())
		print(re_salut())
	elif raspuns == '3':
		print(gol_de_note())
		print(re_salut())
	else:
		print('Ne pare rau, dar nu am inteles ce ati ales.')
		print(re_salut())


salut()
