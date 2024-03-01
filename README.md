# OMRON FINS SIMULATOR
**Introduzione**

Questo script permette al tuo PC con Ruby di funzionare come un PLC virtuale. È stato implementato per il debug di programmi che comunicano con PLC tramite il protocollo FINS.

**Funzionalità**

- Avvia un socket UDP sulla porta specificata (predefinita: 9600) e risponde alle richieste del protocollo FINS.
- Al momento, supporta solo la lettura e la scrittura dell'area DM e l'acquisizione della data/ora.
- Non supporta il protocollo TCP.

**Requisiti**

- Ruby 1.8 o superiore (verificato su Linux, MacOSX e Windows)
- PC con Ruby e il PLC devono essere in grado di comunicare sulla porta UDP 9600 (o altra porta specificata)

**Installazione**

1. Clona il progetto sul tuo PC:

```
git clone https://github.com/hiroeorz/omron-fins-simulator.git
```

2. Esegui il file `omron_plc.rb`, così com'è o copiato in una cartella adatta:

```
ruby omron_plc.rb --address=<IP_address> --port=<port_number>
```

**Esempio di esecuzione:**

```
cd omron-fins-simulator
ruby omron_plc.rb --address=192.168.0.6 --port=9600
```

**Opzioni disponibili:**
```
$ ruby omron_plc.rb --address=192.168.0.6 --port=9600 --count_up_dm=5095 --countup_interval=5 --load_file=/tmp/dm.yaml
```
- `--address`: Indirizzo IP del tuo PC (predefinito: 127.0.0.1)
- `--port`: Numero di porta (predefinito: 9600)
- `--count_up_dm`: Specifica i numeri DM da incrementare automaticamente (separati da virgola)
    * Esempio di specificazione multipla: `--count_up_dm=1,2,3`.
- `--countup_interval`: Intervallo di incremento automatico (predefinito: 5 secondi)
- `--load_file`: File di configurazione DM da caricare all'avvio (formato YAML). Se non viene specificato, tutti i DM sono inizialmente `0`.
    * Il formato del file di configurazione è YAML, dove la chiave è il numero del DM e il valore è il valore del DM.

        ``` 
        3: 0
        100: 11
        101: 21
        102: 0xff
        103: 0x10
        ``` 

**Impostazione e acquisizione di valori in modalità interattiva**

Quando viene attivato, il sistema inizia ad accettare pacchetti UDP sulla porta specificata e attende un input sulla console.

```
$ ruby omron_plc.rb --address=192.168.0.6 --port=9600

Loading /tmp/test.yaml...done
UDP Socket bind to host:192.168.0.6, port:9600.

----------------------------------------------------
PLC SIMULATOR SYSTEM
----------------------------------------------------
SET DM COMMAND     : > set <dm number>, <value>
GET DM COMMAND     : > get <dm number>
GET DM LIST COMMAND: > get_list <dm number>, <count>
EXIT COMMAND       : > exit
----------------------------------------------------

> 
```

Sono disponibili i seguenti comandi:

- `set <dm_number>, <value>`: Imposta il valore nella memoria DM
- `get <dm_number>`: Ottieni il valore dalla memoria DM
- `get_list <dm_number>, <count>`: Ottieni i valori da una serie di indirizzi DM consecutivi
- `exit`: Termina il programma

**Esempio di esecuzione:**

```
$ ruby omron_plc.rb --address=192.168.0.6 --port=9600

Loading /tmp/test.yaml...done
UDP Socket bind to host:172.16.15.35, port:9600.

----------------------------------------------------
PLC SIMULATOR SYSTEM
----------------------------------------------------
SET DM COMMAND     : > set <dm number>, <value>
GET DM COMMAND     : > get <dm number>
GET DM LIST COMMAND: > get_list <dm number>, <count>
EXIT COMMAND       : > exit
----------------------------------------------------

> 
> set 1, 100
ok

> set 2, 200
ok

> set 3, 300
ok

> get_list 1, 3
1 : 100
2 : 200
3 : 300

> exit

$
```

## Docker

Aggiunto un Dockerfile per permettere esecuzione tramite container
Per eseguire build immagine:
```
docker build -t omron/plc-simulator .
```

Per eseguire container

```
docker run -it -p 9600:9600 omron/plc-simulator
```


**Per maggiori informazioni:**

- Consulta il repository GitHub: [https://github.com/hiroeorz/omron-fins-simulator/blob/master/omron_plc.rb](https://github.com/hiroeorz/omron-fins-simulator/blob/master/omron_plc.rb)