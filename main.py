from requests_html import HTMLSession
session = HTMLSession()
payload = {'PaginaAtual': '1',
'NumeroMPTipo': '',
'NumeroMPUA': '',
'NumeroMPSequencial': '',
'NumeroMPAno': '',
'NumeroTJ': '',
'NomeParte': '',
'DocParte': '',
'AssuntoTabUni': '',
'TipoProcedimento': '',
'UA': ''}



r = session.post('https://sismpconsultapublica.mpsp.mp.br/ConsultarProcedimentos/ObterProcedimentos', data=payload, verify=False)

r.html.render()

print(r.html)

