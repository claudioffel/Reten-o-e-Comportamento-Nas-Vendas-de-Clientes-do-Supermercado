select id, nome, bairro, cidade, CAST(datacriacao AS DATE) AS data_criacao  from CADASTRO_PESSOAS where cliente = 1

SELECT
    ecf, 
    CAST(datacupom AS DATE) AS Data_Cupom,
	CONVERT(VARCHAR(8), horacupom, 108) AS Horario,
    cliente,
	coo,
    REPLACE(CAST(totalliquido AS VARCHAR), '.', ',') AS totalliquido, 
    QTDITENS
FROM pdv_cupom
WHERE cliente > 0 
  AND DATACUPOM > '2026-03-31' 
  AND DATACUPOM < '2026-04-22'


  select p.ecf, p.coo, CAST(c.datacupom AS DATE) AS Data_Cupom, c.cliente, p.ean, p.descricao, REPLACE(CAST(p.precovarejo AS VARCHAR), '.', ',') AS preco, REPLACE(CAST(p.QUANTIDADE AS VARCHAR), '.', ',') quantidade
  from PDV_CUPOM_PRODUTOS p inner join pdv_cupom c on p.coo = c.coo and p.ecf = c.ecf and p.datacupom = c.datacupom 
  where c.cliente > 0 and p.cancelado = 0 and p.DATACUPOM > '2026-03-31' AND p.DATACUPOM < '2026-04-22'