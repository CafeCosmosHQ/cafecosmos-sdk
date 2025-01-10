# CafeCosmos SDK 🐍📊☕️


A Python API for CafeCosmos

# Installation 

**You should have python installed**

```bash
git clone https://github.com/CafeCosmosHQ/cafecosmos-sdk.git
cd cafecosmos-sdk

python3 -m venv .venv
source .venv/bin/activate #(or .venv/bin/activate.fish for fish 🐠)

pip3 install -r requirements.txt

jupyter lab autofarm.ipynb #you could also use the vscode jupyter extension
```

---

# **Player Class Documentation**

The `Player` class provides a robust interface for interacting with the `CafeCosmos` game environment. It manages the player's resources, inventory, land operations, crafting, and various game-related activities.


## **Initialization**

### `__init__`
```python
def __init__(world: _World, private_key: Optional[str] = None, env_key_name: Optional[str] = None, land_id: Optional[int] = None) -> None
```

### **Args**
- `world` (_World): An instance of the `World` class that manages game contracts and data.
- `private_key` (Optional[str]): The player's private key (default: `None`).
- `env_key_name` (Optional[str]): The environment variable name for the private key (default: `None`).
- `land_id` (Optional[int]): The player's associated land ID (default: `None`). Automatically selects the first owned land if not provided.

### **Raises**
- `ValueError`: If the specified `land_id` is not owned by the player.

---

## **Player Methods**

### `display_land`
```python
def display_land() -> HTML
```
Displays the player's land as a grid with visual icons for items.

### **Returns**
- `HTML`: The land grid rendered as HTML.

---

### `display_inventory`
```python
def display_inventory() -> HTML
```
Displays the player's inventory with item icons and quantities.

### **Returns**
- `HTML`: The inventory table rendered as HTML.

---

### `place_item`
```python
def place_item(x: int, y: int, item_name: str) -> None
```
Places an item on the player's land.

### **Args**
- `x` (int): The x-coordinate for item placement.
- `y` (int): The y-coordinate for item placement.
- `item_name` (str): The name of the item to place (use `"unlock"` for unlocking).

---

### `create_land`
```python
def create_land(limit_x: int, limit_y: int) -> None
```
Creates a new land for the player.

### **Args**
- `limit_x` (int): The x-dimension size of the land grid.
- `limit_y` (int): The y-dimension size of the land grid.

---

### `find_player_lands`
```python
def find_player_lands(amount_of_lands: int = 0) -> List[int]
```
Finds all lands owned by the player.

### **Args**
- `amount_of_lands` (int): Maximum number of lands to find (default: `0` for unlimited).

### **Returns**
- `List[int]`: A list of land IDs owned by the player.

---

### `get_inventory`
```python
def get_inventory() -> Dict[str, int]
```
Fetches the player's inventory as a dictionary.

### **Returns**
- `Dict[str, int]`: A dictionary mapping item names to quantities.

---

### `get_eth_balance`
```python
def get_eth_balance() -> int
```
Retrieves the player's ETH balance.

### **Returns**
- `int`: The ETH balance in Wei.

---

### `get_leaderboard`
```python
def get_leaderboard() -> pd.DataFrame
```
Fetches the game's leaderboard.

### **Returns**
- `pd.DataFrame`: A DataFrame of leaderboard data.

---

### `transfer_eth`
```python
def transfer_eth(to_address: str, amount: int) -> None
```
Transfers ETH to another address.

### **Args**
- `to_address` (str): The recipient's Ethereum address.
- `amount` (int): The amount of ETH to transfer in Wei.

---

### `craft_item`
```python
def craft_item(item_name: str, quantity: int = 1) -> None
```
Crafts an item using the player's inventory.

### **Args**
- `item_name` (str): The name of the item to craft.
- `quantity` (int): Number of items to craft (default: `1`).

---

### `get_craftable`
```python
def get_craftable() -> pd.DataFrame
```
Retrieves a list of craftable items based on the player's inventory.

### **Returns**
- `pd.DataFrame`: A DataFrame of craftable items and their required resources.

---

### `time_until_unlock`
```python
def time_until_unlock(x: int, y: int) -> int
```
Calculates the time remaining for an item at `(x, y)` to unlock.

### **Args**
- `x` (int): The x-coordinate of the item.
- `y` (int): The y-coordinate of the item.

### **Returns**
- `int`: Time in seconds until the item unlocks (or `0` if already unlocked).

---

### `get_unlockable_transformations`
```python
def get_unlockable_transformations() -> Dict[str, Optional[List[Tuple[int, int]]]]
```
Fetches items on the player's land that can be unlocked.

### **Returns**
- `Dict[str, Optional[List[Tuple[int, int]]]]`: A dictionary with unlockable coordinates and the next unlock time.

---

### `unlock_all`
```python
def unlock_all() -> List[Tuple[int, int]]
```
Unlocks all currently unlockable items on the player's land.

### **Returns**
- `List[Tuple[int, int]]`: A list of coordinates for failed unlock attempts.

---

### `auto_farm`
```python
def auto_farm() -> None
```
Automatically farms resources by unlocking items as they become available.

---

## **Static Methods**

### `name_to_id_fuzzy`
```python
@staticmethod
def name_to_id_fuzzy(name: str, threshold: int = 80) -> int
```
Matches a fuzzy item name to its ID.

### **Args**
- `name` (str): The item name to match.
- `threshold` (int): Fuzzy matching score threshold (default: `80`).

### **Returns**
- `int`: The matching item ID.

---

### `id_to_name`
```python
@staticmethod
def id_to_name(id: int) -> str
```
Maps an item ID to its name.

### **Args**
- `id` (int): The item ID.

### **Returns**
- `str`: The item name.

---

## **Game Utilities**

- **Land Display**: Renders the player's land with visual icons.
- **Inventory Management**: Tracks item quantities with graphical outputs.
- **Crafting**: Automates crafting based on available resources.
- **Resource Farming**: Unlocks and farms resources in real-time.
- **Ethereum Interactions**: Supports ETH transfers and balance checks.

---

### Note:
For smooth operation, ensure external dependencies such as `Items.csv`, `Web3`, and contract ABI files are correctly configured.
