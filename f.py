f = open('h.txt', 'w')
t=33
d=13
for y in range(0,4):
	st='<tr><td>{}</td><td>{}</td>'.format(t,d)
	d+=1
	for x in range(0,6):
		st+='<td>{}</td>'.format(d)
		d+=1
	st+='</tr>'
	f.write(st+'\n')
	t+=1
	d+=1

f.close()