import requests


def get_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json'.format(cep))
    cep_data = response.json()
    return cep_data


if __name__ == "__main__":
    print(get_cep('01001000'))
