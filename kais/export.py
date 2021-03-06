# encoding: utf-8

from djcopybook.fixedwidth import Record
from djcopybook.fixedwidth import fields


class NullDecimalField(fields.DecimalField):

    def to_record(self, val):
        if val is None:
            return fields.str_padding(self.length, '')
        else:
            val = round(val, 2)
            return super(NullDecimalField, self).to_record(val)


class SignedNullDecimalField(fields.DecimalField):

    def to_record(self, val):
        if val is None:
            return fields.str_padding(self.length, '')
        else:
            val = round(val, 2)
            negative = val < 0
            val = abs(val)
            res = super(SignedNullDecimalField, self).to_record(val)
            if negative:
                res = list(res)
                res[0] = '-'
            return ''.join(res)


class StringFieldAutoTruncated(fields.StringField):

    def to_record(self, val):
        self.auto_truncate = True
        return super(StringFieldAutoTruncated, self).to_record(val)


class AccountMoveLine(Record):
    codi_empr = StringFieldAutoTruncated(length=2)
    exercici = StringFieldAutoTruncated(length=4)
    data_assent = fields.DateField(length=8, format="%Y%m%d")
    data_doc = fields.DateField(length=8, format="%Y%m%d")
    document = StringFieldAutoTruncated(length=10)
    codi_cto = StringFieldAutoTruncated(length=2)
    descr_cto = StringFieldAutoTruncated(length=30)
    deure = SignedNullDecimalField(length=16, decimals=6)
    haver = SignedNullDecimalField(length=16, decimals=6)
    codi_compte = StringFieldAutoTruncated(length=12)
    diari = StringFieldAutoTruncated(length=2)
    num_provisional = NullDecimalField(length=6, decimals=0)
    descr_compte = StringFieldAutoTruncated(length=30)
    domicili = StringFieldAutoTruncated(length=30)
    codipostal = StringFieldAutoTruncated(length=5)
    poblacio = StringFieldAutoTruncated(length=30)
    nif = StringFieldAutoTruncated(length=15)
    banc = StringFieldAutoTruncated(length=4)
    agencia = StringFieldAutoTruncated(length=4)
    compte_banc = StringFieldAutoTruncated(length=12)
    adr_agencia = StringFieldAutoTruncated(length=25)
    annex_iva = StringFieldAutoTruncated(length=2)
    serie_iva = StringFieldAutoTruncated(length=2)
    nom_prov = StringFieldAutoTruncated(length=30)
    nif_prov = StringFieldAutoTruncated(length=15)
    total_fra = NullDecimalField(length=16, decimals=6)
    tipo_base1 = StringFieldAutoTruncated(length=1)
    base1 = SignedNullDecimalField(length=16, decimals=6)
    perc_iva1 = NullDecimalField(length=5, decimals=2)
    perc_rec1 = NullDecimalField(length=5, decimals=2)
    imp_iva1 = SignedNullDecimalField(length=16, decimals=6)
    imp_rec1 = NullDecimalField(length=16, decimals=6)
    tipo_base2 = StringFieldAutoTruncated(length=1)
    base2 = NullDecimalField(length=16, decimals=6)
    perc_iva2 = NullDecimalField(length=5, decimals=2)
    perc_rec2 = NullDecimalField(length=5, decimals=2)
    imp_iva2 = NullDecimalField(length=16, decimals=6)
    imp_rec2 = NullDecimalField(length=16, decimals=6)
    tipo_base3 = StringFieldAutoTruncated(length=1)
    base3 = NullDecimalField(length=16, decimals=6)
    perc_iva3 = NullDecimalField(length=5, decimals=2)
    perc_rec3 = NullDecimalField(length=5, decimals=2)
    imp_iva3 = NullDecimalField(length=16, decimals=6)
    imp_rec3 = NullDecimalField(length=16, decimals=6)
    tipo_base4 = StringFieldAutoTruncated(length=1)
    base4 = NullDecimalField(length=16, decimals=6)
    perc_iva4 = NullDecimalField(length=5, decimals=2)
    perc_rec4 = NullDecimalField(length=5, decimals=2)
    imp_iva4 = NullDecimalField(length=16, decimals=6)
    imp_rec4 = NullDecimalField(length=16, decimals=6)
    annex_cart = StringFieldAutoTruncated(length=2)
    banc_cart = StringFieldAutoTruncated(length=4)
    agencia_cart = StringFieldAutoTruncated(length=4)
    compte_cart = StringFieldAutoTruncated(length=12)
    descr_agen_cart = StringFieldAutoTruncated(length=25)
    dcp_codi = StringFieldAutoTruncated(length=2)
    cls_codi = StringFieldAutoTruncated(length=2)
    scp_codi = StringFieldAutoTruncated(length=2)
    data_venc1 = fields.DateField(length=8, format="%Y%m%d")
    import_venc1 = NullDecimalField(length=16, decimals=6)
    data_venc2 = fields.DateField(length=8, format="%Y%m%d")
    import_venc2 = NullDecimalField(length=16, decimals=6)
    data_venc3 = fields.DateField(length=8, format="%Y%m%d")
    import_venc3 = NullDecimalField(length=16, decimals=6)
    data_venc4 = fields.DateField(length=8, format="%Y%m%d")
    import_venc4 = NullDecimalField(length=16, decimals=6)
    data_venc5 = fields.DateField(length=8, format="%Y%m%d")
    import_venc5 = NullDecimalField(length=16, decimals=6)
    data_venc6 = fields.DateField(length=8, format="%Y%m%d")
    import_venc6 = NullDecimalField(length=16, decimals=6)
    cta_prv_iva = StringFieldAutoTruncated(length=12)
    divisa = StringFieldAutoTruncated(length=3)
    cambio = NullDecimalField(length=12, decimals=6)
    centro = StringFieldAutoTruncated(length=6)
    divimportedebe = NullDecimalField(length=16, decimals=6)
    divimportehaber = NullDecimalField(length=16, decimals=6)
    divimporteven1 = NullDecimalField(length=16, decimals=6)
    divimporteven2 = NullDecimalField(length=16, decimals=6)
    divimporteven3 = NullDecimalField(length=16, decimals=6)
    divimporteven4 = NullDecimalField(length=16, decimals=6)
    divimporteven5 = NullDecimalField(length=16, decimals=6)
    divimporteven6 = NullDecimalField(length=16, decimals=6)
    codigodivisacliente = StringFieldAutoTruncated(length=3)
    descripciondivisacliente = StringFieldAutoTruncated(length=25)
    abreviaciondivisacliente = StringFieldAutoTruncated(length=3)
    dpdivisacliente = fields.IntegerField(length=1)
    didivisacliente = fields.IntegerField(length=1)
    cotizaciondivisacliente = NullDecimalField(length=12, decimals=6)
    codigopaiscliente = StringFieldAutoTruncated(length=3)
    nombrepaiscliente = StringFieldAutoTruncated(length=30)
    rivapaiscliente = fields.IntegerField(length=1)
    intrastatpaiscliente = StringFieldAutoTruncated(length=3)
    agentecliente = StringFieldAutoTruncated(length=3)
    provinciacliente = StringFieldAutoTruncated(length=35)
    tipodocs = StringFieldAutoTruncated(length=12)
    negociablesdocs = StringFieldAutoTruncated(length=12)
    data_venc7 = fields.DateField(length=8, format="%Y%m%d")
    data_venc8 = fields.DateField(length=8, format="%Y%m%d")
    data_venc9 = fields.DateField(length=8, format="%Y%m%d")
    data_venc10 = fields.DateField(length=8, format="%Y%m%d")
    data_venc11 = fields.DateField(length=8, format="%Y%m%d")
    data_venc12 = fields.DateField(length=8, format="%Y%m%d")
    import_venc7 = NullDecimalField(length=16, decimals=6)
    import_venc8 = NullDecimalField(length=16, decimals=6)
    import_venc9 = NullDecimalField(length=16, decimals=6)
    import_venc10 = NullDecimalField(length=16, decimals=6)
    import_venc11 = NullDecimalField(length=16, decimals=6)
    import_venc12 = NullDecimalField(length=16, decimals=6)
    divimporteven7 = NullDecimalField(length=16, decimals=6)
    divimporteven8 = NullDecimalField(length=16, decimals=6)
    divimporteven9 = NullDecimalField(length=16, decimals=6)
    divimporteven10 = NullDecimalField(length=16, decimals=6)
    divimporteven11 = NullDecimalField(length=16, decimals=6)
    divimporteven12 = NullDecimalField(length=16, decimals=6)
    negociablesdocs2 = StringFieldAutoTruncated(length=12)
    tipodocs2 = StringFieldAutoTruncated(length=12)
    cobrador = StringFieldAutoTruncated(length=3)
    cobnom = StringFieldAutoTruncated(length=35)
    responsable = StringFieldAutoTruncated(length=10)
    respnom = StringFieldAutoTruncated(length=30)
    formapago = StringFieldAutoTruncated(length=3)
    diapago1 = NullDecimalField(length=2, decimals=0)
    diapago2 = NullDecimalField(length=2, decimals=0)
    diapago3 = NullDecimalField(length=2, decimals=0)
    centrecodi1 = StringFieldAutoTruncated(length=16)
    centretext1 = StringFieldAutoTruncated(length=35)
    centrecodi2 = StringFieldAutoTruncated(length=16)
    centretext2 = StringFieldAutoTruncated(length=35)
    centrecodi3 = StringFieldAutoTruncated(length=16)
    centretext3 = StringFieldAutoTruncated(length=35)
    centrecodi4 = StringFieldAutoTruncated(length=16)
    centretext4 = StringFieldAutoTruncated(length=35)
    centrecodi5 = StringFieldAutoTruncated(length=16)
    centretext5 = StringFieldAutoTruncated(length=35)
    seriefra = StringFieldAutoTruncated(length=2)
    dia_nom = StringFieldAutoTruncated(length=40)
    cobobserva = StringFieldAutoTruncated(length=200)
    criteriocoste = StringFieldAutoTruncated(length=6)
    rupturaccoste = StringFieldAutoTruncated(length=6)
    nifampliado = StringFieldAutoTruncated(length=15)
    documentoampliado = StringFieldAutoTruncated(length=25)
    iban = StringFieldAutoTruncated(length=34)
    swift = StringFieldAutoTruncated(length=11)
    esp_tipoapunte = StringFieldAutoTruncated(length=10)
    tiqueini = StringFieldAutoTruncated(length=20)
    tiquefin = StringFieldAutoTruncated(length=20)
    localizador = StringFieldAutoTruncated(length=25)
    compraregivafinanigualnumfactprov = StringFieldAutoTruncated(length=1)
    compranumfactregivafinanigualnumfactprov = StringFieldAutoTruncated(length=1)
    compranumfactcartpagfinanigualnumfactprov = StringFieldAutoTruncated(length=1)
    compranumfactprov = StringFieldAutoTruncated(length=20)
    tipoidentdoc = StringFieldAutoTruncated(length=2)


if __name__ == '__main__':
    from datetime import date
    m = AccountMoveLine(
        data_assent = date(2018, 5, 28),
        data_doc=date(2018, 5, 27),
        document="F43453543",
        codi_cto="01",
        descr_cto="P1",
        deure=200.43,
        haver=0,
        codi_compte="70000004",
        diari="01",
        num_provisional=4353,
        descr_compte="Hacienda Pública. IVA repercutido 21%"
    )
    print(m.to_record())