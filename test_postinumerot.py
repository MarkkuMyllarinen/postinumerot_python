import pytest
import postinumerot

def test_etsi_postinumerot():       # annettua nimeä ei löydy lainkaan aineistosta
    assert len(postinumerot.etsi_postinumerot("kaupunkijokaeipalautamitään",postinumerot.postinumero_lista())) == 0

def test_yksi_postinumero():        # postitoimipaikan nimellä löytyy yksi postinumero
    assert len(postinumerot.etsi_postinumerot("niittylahti",postinumerot.postinumero_lista())) == 1

def test_monta_postinumero():       # postitoimipaikan nimellä löytyy useita postinumeroita
    assert len(postinumerot.etsi_postinumerot("Espoo",postinumerot.postinumero_lista())) > 2
