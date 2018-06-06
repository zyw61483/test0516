import ExcelUtil
import FileUtil

dict = ExcelUtil.get(r"C:\Users\zhaoyiwei\Desktop\超时还款记录\超时还款记录0604.xlsx",1,1)
result = []
target = '{{"repayOuterNo":"{0}","loanOuterNo":"{1}","repayTime":"{2}","status":{3},"outterMessage":"","repaySource":{4},"repayPlanListString":"[{{\"repayPlanId\":{5},\"principal\":{6},\"breach\":0,\"charge\":0,\"interest\":{7},\"earlyRepayBreach\":0,\"penalty\":0,\"installmentNo\":{8}}}]" }}'
# target1 = '{{"repayOuterNo":"{0}"}}'
for key in dict:
	line = dict[key]
	print(line)
	temp = target.format(line[0].strip(),line[1].strip(),line[3].strip(),round(line[4]),round(line[5]),line[6],line[7],line[10],line[13])
	# print(line[0])
	# temp = target.format(line[0].strip())
	print(temp)
	result.append(temp)

FileUtil.write(r"C:\Users\zhaoyiwei\Desktop\123\666.txt","a+",result)