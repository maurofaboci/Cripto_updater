{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "624dfcea",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Imports \n",
    "\n",
    "from selenium import webdriver\n",
    "from selenium.webdriver.common.by import By\n",
    "from selenium.webdriver.support.ui import WebDriverWait\n",
    "from selenium.webdriver.support import expected_conditions as EC\n",
    "from selenium.webdriver.common.keys import Keys"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "176d8a33",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "# Navegando nas paginas para pegar a cotação atual das moedas (Navegação MILK)\n",
    "\n",
    "navegador = webdriver.Chrome()\n",
    "navegador.get(\"https://poocoin.app/tokens/0xbf37f781473f3b50e82c668352984865eac9853f\")\n",
    "cotacao_milk = WebDriverWait(navegador, 10).until(\n",
    "        EC.presence_of_element_located((By.XPATH, '//*[@id=\"root\"]/div/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/div[1]/div/span'))).text\n",
    "navegador.quit()\n",
    "\n",
    "#print(cotacao_milk.replace(\"$\", ''))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "7c479dbc",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Navegando nas paginas para pegar a cotação atual das moedas (Navegação THC)\n",
    "\n",
    "navegador = webdriver.Chrome()\n",
    "navegador.get(\"https://poocoin.app/tokens/0x24802247bd157d771b7effa205237d8e9269ba8a\")\n",
    "cotacao_thc = WebDriverWait(navegador, 10).until(\n",
    "        EC.presence_of_element_located((By.XPATH, '//*[@id=\"root\"]/div/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/div[1]/div/span'))).text\n",
    "navegador.quit()\n",
    "\n",
    "#print(cotacao_thc.replace(\"$\", ''))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "081621a8",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Navegando nas paginas para pegar a cotação atual das moedas (Navegação THG)\n",
    "\n",
    "navegador = webdriver.Chrome()\n",
    "navegador.get(\"https://poocoin.app/tokens/0x9fd87aefe02441b123c3c32466cd9db4c578618f\")\n",
    "cotacao_thg = WebDriverWait(navegador, 10).until(\n",
    "        EC.presence_of_element_located((By.XPATH, '//*[@id=\"root\"]/div/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/div[1]/div/span'))).text\n",
    "navegador.quit()\n",
    "\n",
    "#print(cotacao_thg.replace(\"$\", ''))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "04283b15",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Navegando nas paginas para pegar a cotação atual das moedas (Navegação MAFA)\n",
    "\n",
    "navegador = webdriver.Chrome()\n",
    "navegador.get(\"https://poocoin.app/tokens/0xaf44400a99a9693bf3c2e89b02652babacc5cdb9\")\n",
    "cotacao_mafa = WebDriverWait(navegador, 10).until(\n",
    "        EC.presence_of_element_located((By.XPATH, '//*[@id=\"root\"]/div/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/div[1]/div/span'))).text\n",
    "navegador.quit()\n",
    "\n",
    "#print(cotacao_mafa.replace(\"$\", ''))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "8c261dce",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Navegando nas paginas para pegar a cotação atual das moedas (Navegação DRACO)\n",
    "\n",
    "navegador = webdriver.Chrome()\n",
    "navegador.get(\"https://www.mir4draco.com/price\")\n",
    "cotacao_draco = WebDriverWait(navegador, 30).until(\n",
    "        EC.presence_of_element_located((By.XPATH, '//*[@id=\"app\"]/div/div/main/div/section[2]/div[1]/div/div[1]/div/div[4]/div/div/dl/dd/span[1]'))).text\n",
    "navegador.quit()\n",
    "\n",
    "#print(cotacao_draco.replace(\"$\", ''))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "0bd1b63b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['$0.000913698', '$0.0667472', '$4.1436', '$0.0498955', '$0.7760']\n",
      "['0.000913698', '0.0667472', '4.1436', '0.0498955', '0.7760']\n"
     ]
    }
   ],
   "source": [
    "#Tratando as moedas para poder converter a FLOAT na tabela (tive dificuldade de mudar dois valores em um só for)\n",
    "\n",
    "moedasdlr = [cotacao_milk, cotacao_thc, cotacao_thg, cotacao_mafa, cotacao_draco]\n",
    "moedas = []\n",
    "for num in moedasdlr: \n",
    "    moedasnew = num.replace(\",\",\".\")\n",
    "    moedas.append(moedasnew)\n",
    "print(moedas)\n",
    "\n",
    "moedasok = []\n",
    "for num in moedas: \n",
    "    moedasnew = num.replace(\"$\",\"\")\n",
    "    moedasok.append(moedasnew)\n",
    "print(moedasok)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "15dc0cbd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Unnamed: 0</th>\n",
       "      <th>Jogo</th>\n",
       "      <th>Moeda</th>\n",
       "      <th>Data entrada</th>\n",
       "      <th>Data Saida</th>\n",
       "      <th>Tempo investindo</th>\n",
       "      <th>Qt_Moedas</th>\n",
       "      <th>cotacao compra</th>\n",
       "      <th>cotacao atual</th>\n",
       "      <th>Vl_investido</th>\n",
       "      <th>Vl_recebido</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Mir4</td>\n",
       "      <td>DRACO</td>\n",
       "      <td>2021-11-01</td>\n",
       "      <td>2022-01-17</td>\n",
       "      <td>77</td>\n",
       "      <td>214.00</td>\n",
       "      <td>0.56</td>\n",
       "      <td>0.771700</td>\n",
       "      <td>119.8400</td>\n",
       "      <td>165.143800</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>Thetan arena</td>\n",
       "      <td>THG</td>\n",
       "      <td>2021-12-29</td>\n",
       "      <td>2022-01-17</td>\n",
       "      <td>19</td>\n",
       "      <td>1078.37</td>\n",
       "      <td>5.04</td>\n",
       "      <td>4.150400</td>\n",
       "      <td>5434.9848</td>\n",
       "      <td>4475.666848</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>Thetan arena</td>\n",
       "      <td>THC</td>\n",
       "      <td>2021-12-09</td>\n",
       "      <td>2022-01-17</td>\n",
       "      <td>39</td>\n",
       "      <td>8322.16</td>\n",
       "      <td>0.13</td>\n",
       "      <td>0.066827</td>\n",
       "      <td>1081.8808</td>\n",
       "      <td>556.144986</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Mafagafu</td>\n",
       "      <td>MAFA</td>\n",
       "      <td>2021-11-26</td>\n",
       "      <td>2022-01-17</td>\n",
       "      <td>52</td>\n",
       "      <td>795.81</td>\n",
       "      <td>0.09</td>\n",
       "      <td>0.049959</td>\n",
       "      <td>71.6229</td>\n",
       "      <td>39.757713</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>Criptoyou</td>\n",
       "      <td>MILK</td>\n",
       "      <td>2021-11-01</td>\n",
       "      <td>2022-01-17</td>\n",
       "      <td>77</td>\n",
       "      <td>1369.97</td>\n",
       "      <td>0.01</td>\n",
       "      <td>0.000914</td>\n",
       "      <td>13.6997</td>\n",
       "      <td>1.252103</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Unnamed: 0          Jogo  Moeda Data entrada Data Saida  Tempo investindo   \\\n",
       "0           0          Mir4  DRACO   2021-11-01 2022-01-17                 77   \n",
       "1           1  Thetan arena    THG   2021-12-29 2022-01-17                 19   \n",
       "2           2  Thetan arena    THC   2021-12-09 2022-01-17                 39   \n",
       "3           3      Mafagafu   MAFA   2021-11-26 2022-01-17                 52   \n",
       "4           4     Criptoyou   MILK   2021-11-01 2022-01-17                 77   \n",
       "\n",
       "   Qt_Moedas  cotacao compra  cotacao atual  Vl_investido  Vl_recebido  \n",
       "0     214.00            0.56       0.771700      119.8400   165.143800  \n",
       "1    1078.37            5.04       4.150400     5434.9848  4475.666848  \n",
       "2    8322.16            0.13       0.066827     1081.8808   556.144986  \n",
       "3     795.81            0.09       0.049959       71.6229    39.757713  \n",
       "4    1369.97            0.01       0.000914       13.6997     1.252103  "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#importando a tabela \n",
    "import pandas as pd\n",
    "\n",
    "tabela = pd.read_excel(\"tabela.xlsx\")\n",
    "\n",
    "display(tabela)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "5ff8d792",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Unnamed: 0</th>\n",
       "      <th>Jogo</th>\n",
       "      <th>Moeda</th>\n",
       "      <th>Data entrada</th>\n",
       "      <th>Data Saida</th>\n",
       "      <th>Tempo investindo</th>\n",
       "      <th>Qt_Moedas</th>\n",
       "      <th>cotacao compra</th>\n",
       "      <th>cotacao atual</th>\n",
       "      <th>Vl_investido</th>\n",
       "      <th>Vl_recebido</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Mir4</td>\n",
       "      <td>DRACO</td>\n",
       "      <td>2021-11-01</td>\n",
       "      <td>2022-01-17</td>\n",
       "      <td>77</td>\n",
       "      <td>214.00</td>\n",
       "      <td>0.56</td>\n",
       "      <td>0.776000</td>\n",
       "      <td>119.8400</td>\n",
       "      <td>166.064000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>Thetan arena</td>\n",
       "      <td>THG</td>\n",
       "      <td>2021-12-29</td>\n",
       "      <td>2022-01-17</td>\n",
       "      <td>19</td>\n",
       "      <td>1078.37</td>\n",
       "      <td>5.04</td>\n",
       "      <td>4.143600</td>\n",
       "      <td>5434.9848</td>\n",
       "      <td>4468.333932</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>Thetan arena</td>\n",
       "      <td>THC</td>\n",
       "      <td>2021-12-09</td>\n",
       "      <td>2022-01-17</td>\n",
       "      <td>39</td>\n",
       "      <td>8322.16</td>\n",
       "      <td>0.13</td>\n",
       "      <td>0.066747</td>\n",
       "      <td>1081.8808</td>\n",
       "      <td>555.480878</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Mafagafu</td>\n",
       "      <td>MAFA</td>\n",
       "      <td>2021-11-26</td>\n",
       "      <td>2022-01-17</td>\n",
       "      <td>52</td>\n",
       "      <td>795.81</td>\n",
       "      <td>0.09</td>\n",
       "      <td>0.049896</td>\n",
       "      <td>71.6229</td>\n",
       "      <td>39.707338</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>Criptoyou</td>\n",
       "      <td>MILK</td>\n",
       "      <td>2021-11-01</td>\n",
       "      <td>2022-01-17</td>\n",
       "      <td>77</td>\n",
       "      <td>1369.97</td>\n",
       "      <td>0.01</td>\n",
       "      <td>0.000914</td>\n",
       "      <td>13.6997</td>\n",
       "      <td>1.251739</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Unnamed: 0          Jogo  Moeda Data entrada Data Saida  Tempo investindo   \\\n",
       "0           0          Mir4  DRACO   2021-11-01 2022-01-17                 77   \n",
       "1           1  Thetan arena    THG   2021-12-29 2022-01-17                 19   \n",
       "2           2  Thetan arena    THC   2021-12-09 2022-01-17                 39   \n",
       "3           3      Mafagafu   MAFA   2021-11-26 2022-01-17                 52   \n",
       "4           4     Criptoyou   MILK   2021-11-01 2022-01-17                 77   \n",
       "\n",
       "   Qt_Moedas  cotacao compra  cotacao atual  Vl_investido  Vl_recebido  \n",
       "0     214.00            0.56       0.776000      119.8400   166.064000  \n",
       "1    1078.37            5.04       4.143600     5434.9848  4468.333932  \n",
       "2    8322.16            0.13       0.066747     1081.8808   555.480878  \n",
       "3     795.81            0.09       0.049896       71.6229    39.707338  \n",
       "4    1369.97            0.01       0.000914       13.6997     1.251739  "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#atualizando a tabela com as cotações atuais\n",
    "\n",
    "tabela.loc[tabela['Moeda'] == 'DRACO','cotacao atual'] = float(moedasok[4])\n",
    "tabela.loc[tabela['Moeda'] == 'THG','cotacao atual'] = float(moedasok[2])\n",
    "tabela.loc[tabela['Moeda'] == 'THC','cotacao atual'] = float(moedasok[1])\n",
    "tabela.loc[tabela['Moeda'] == 'MAFA','cotacao atual'] = float(moedasok[3])\n",
    "tabela.loc[tabela['Moeda'] == 'MILK','cotacao atual'] = float(moedasok[0])\n",
    "\n",
    "#atualizando os valores totais \n",
    "\n",
    "tabela[\"Vl_recebido\"] = tabela[\"Qt_Moedas\"] * tabela[\"cotacao atual\"]\n",
    "\n",
    "display(tabela)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "5f5498a5",
   "metadata": {},
   "outputs": [],
   "source": [
    "#salvando a tabela na pasta\n",
    "tabela.to_excel(\"tabela.xlsx\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "02d9c944",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting pyinstaller\n",
      "  Downloading pyinstaller-4.8-py3-none-win_amd64.whl (2.0 MB)\n",
      "Requirement already satisfied: pywin32-ctypes>=0.2.0 in c:\\users\\55119\\anaconda3\\lib\\site-packages (from pyinstaller) (0.2.0)\n",
      "Requirement already satisfied: setuptools in c:\\users\\55119\\anaconda3\\lib\\site-packages (from pyinstaller) (58.0.4)\n",
      "Collecting pefile>=2017.8.1\n",
      "  Downloading pefile-2021.9.3.tar.gz (72 kB)\n",
      "  Preparing metadata (setup.py): started\n",
      "  Preparing metadata (setup.py): finished with status 'done'\n",
      "Collecting pyinstaller-hooks-contrib>=2020.6\n",
      "  Downloading pyinstaller_hooks_contrib-2021.5-py2.py3-none-any.whl (216 kB)\n",
      "Collecting altgraph\n",
      "  Downloading altgraph-0.17.2-py2.py3-none-any.whl (21 kB)\n",
      "Requirement already satisfied: future in c:\\users\\55119\\anaconda3\\lib\\site-packages (from pefile>=2017.8.1->pyinstaller) (0.18.2)\n",
      "Building wheels for collected packages: pefile\n",
      "  Building wheel for pefile (setup.py): started\n",
      "  Building wheel for pefile (setup.py): finished with status 'done'\n",
      "  Created wheel for pefile: filename=pefile-2021.9.3-py3-none-any.whl size=68844 sha256=739eafaffcb07e8c1eb3274ba04e65dd4dd5dde838ed2ab3e223a9dad16b45dd\n",
      "  Stored in directory: c:\\users\\55119\\appdata\\local\\pip\\cache\\wheels\\05\\42\\e9\\7d0273e82936b525e10e4080595cd0aad0b3481d78b5a3aecc\n",
      "Successfully built pefile\n",
      "Installing collected packages: pyinstaller-hooks-contrib, pefile, altgraph, pyinstaller\n",
      "Successfully installed altgraph-0.17.2 pefile-2021.9.3 pyinstaller-4.8 pyinstaller-hooks-contrib-2021.5\n"
     ]
    }
   ],
   "source": [
    "!pip install pyinstaller\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "f3b3895a",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'pyinstaller' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_7992/1289571781.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mpyinstaller\u001b[0m \u001b[1;33m-\u001b[0m\u001b[1;33m-\u001b[0m\u001b[0monefile\u001b[0m \u001b[1;33m-\u001b[0m\u001b[0mw\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'pyinstaller' is not defined"
     ]
    }
   ],
   "source": [
    "pyinstaller --onefile -w"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "30e0ff0f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
