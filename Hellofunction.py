from re import S


def Give_accsess_to_devs(s):
    for name in s:
        if (name == "Aleksander"):
            print("Får ikke tilgang: ", name)
        else:
            print("Du får tilgang: ",  name)

utviklere_som_skal_ha_adgang = ["Aleksander","Torsvik","Torsvik UwU","Vegard","Olav UwU"]

Give_accsess_to_devs(utviklere_som_skal_ha_adgang)