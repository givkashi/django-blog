from . import jalali
from django.utils import timezone

def persian_numbers_conventer(mystr):
	numbers = {
		"0" : "",
		"1" : "",
		"2" : "",
		"3" : "",
		"4" : "",
		"5" : "",
		"6" : "",
		"7" : "",
		"8" : "",
		"9" : "",
	}

	for e, p in numbers.items():
		mystr = mystr.replace(e,p)

	return mystr


def jalali_converter(time):
	jmonths=[ "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند" ]

	time= timezone.localtime(time)

	time_to_str= "{},{},{}".format(time.year,time.month,time.day)
	time_to_tuple= jalali.Gregorian(time_to_str).persian_tuple()
	
	time_to_list = list(time_to_tuple)

	for index, month in enumerate(jmonths):
		if time_to_list[1] == index + 1:
			time_to_list[1]=month
			break


	output = "{} {} {} , ساعت   {}:{}".format(
			time_to_list[2],
			time_to_list[1],
			time_to_list[0],
			time.hour,
			time.minute,

		)
	return  output
	#return  persian_numbers_conventer(output) baraye farsi nevisi adad az in tabe estefade mikonim