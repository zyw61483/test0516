#! usr/bin/python3

def organize(file):
	dict = {}
	for line in file:
		list = line[:-1].split("\t")
		# list = line.replace("\n","").split("\t")
		dict.update({list[0].strip():list[1].strip()})
	return dict

sql = "UPDATE fcp_fe_bjbiz_telecom_00.fcp_tel_user_identity SET sync_account_fail_times = 0,cert_back_image='{}' where user_id={};\n"
with open("C:\\Users\\zhaoyiwei\\Desktop\\document\\数据订正\\身份证背面\\a.txt","r") as a_file:
	a_dict = organize(a_file)
	with open("C:\\Users\\zhaoyiwei\\Desktop\\document\\数据订正\\身份证背面\\b.txt","r") as b_file:
		b_dict = organize(b_file)
		with open("C:\\Users\\zhaoyiwei\\Desktop\\document\\数据订正\\身份证背面\\c.txt","w") as c_file:
			for akey in a_dict:
				for bkey in b_dict:
					if akey == b_dict[bkey] :
						print("{}\t{}".format(akey,b_dict[bkey]))
						c_file.write(sql.format(a_dict[akey],bkey))
						
						
# a_file = open("C:\\Users\\zhaoyiwei\\Desktop\\document\\数据订正\\身份证背面\\a.txt","r")
# b_file = open("C:\\Users\\zhaoyiwei\\Desktop\\document\\数据订正\\身份证背面\\b.txt","r")
# c_file = open("C:\\Users\\zhaoyiwei\\Desktop\\document\\数据订正\\身份证背面\\c.txt","w")

# a_dict = organize(a_file)
# b_dict = organize(b_file)
	# for akey in a_dict:
	# for bkey in b_dict:
		# if akey == b_dict[bkey] :
			# print("{}\t{}".format(akey,b_dict[bkey]))
			# c_file.write(sql.format(a_dict[akey],bkey))

# a_file.close()
# b_file.close()
# c_file.close()
