from lastpass import Vault
from pyperclip import copy
from wox import Wox

class Lastpass(Wox):
    def query(self, Query):
        Results = []

        if len(Query) > 0:
            LPVault = Vault.open_remote('<LASTPASS VAULT USERNAME>', '<LASTPASS VAULT PASSWORD>')
            for LPEntry in LPVault.accounts:
                Name = LPEntry.name.decode('utf-8')
                if Name.lower() == Query.lower():
                    Results.append({
                        'Title': Name,
                        'SubTitle': 'Copy Username from "{}"'.format(Name),
                        'IcoPath': 'Images/lp_username.ico',
                        'JsonRPCAction': {
                            'method': 'copy_to_clipboard',
                            'parameters': [
                                LPEntry.username.decode('utf-8')
                            ]
                        }
                    })
                    Results.append({
                        'Title': Name,
                        'SubTitle': 'Copy Password from "{}"'.format(Name),
                        'IcoPath': 'Images/lp_password.ico',
                        'JsonRPCAction': {
                            'method': 'copy_to_clipboard',
                            'parameters': [
                                LPEntry.password.decode('utf-8')
                            ]
                        }
                    })
                    break

        return Results

    def copy_to_clipboard(self, Data):
        copy(Data)

if __name__ == "__main__":
    Lastpass()
