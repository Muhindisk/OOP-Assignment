class Smartphone:
    def __init__(self, brand, model, storage, color, battery_level=100):
        self.brand = brand
        self.model = model
        self._storage = storage  # Encapsulated attribute
        self.color = color
        self.battery_level = battery_level
        self.is_locked = True
        self._pin = "1234"  # Encapsulated attribute
    
    def unlock(self, pin):
        if pin == self._pin:
            self.is_locked = False
            return f"{self.brand} {self.model} unlocked successfully! 🔓"
        else:
            return "Incorrect PIN! ❌"
    
    def lock(self):
        self.is_locked = True
        return f"{self.brand} {self.model} is now locked. 🔒"
    
    def make_call(self, number):
        if self.battery_level <= 5:
            return "Battery too low to make a call! ⚡"
        if self.is_locked:
            return "Please unlock the phone first! 🔒"
        
        self.battery_level -= 5
        return f"Calling {number}... 📞"
    
    def send_message(self, number, message):
        if self.battery_level <= 2:
            return "Battery too low to send a message! ⚡"
        if self.is_locked:
            return "Please unlock the phone first! 🔒"
        if len(message) > 160:
            return "Message too long! Maximum 160 characters. ❌"
        
        self.battery_level -= 2
        return f"Message sent to {number}: '{message}' 💬"
    
    def charge(self, minutes):
        charge_amount = min(minutes * 2, 100 - self.battery_level)
        self.battery_level += charge_amount
        return f"Charged for {minutes} minutes. Battery now at {self.battery_level}% 🔋"
    
    # Encapsulation with getter and setter
    @property
    def storage(self):
        return f"{self._storage}GB"
    
    @storage.setter
    def storage(self, value):
        print("Storage cannot be changed after purchase! ❌")
    
    def change_pin(self, old_pin, new_pin):
        if old_pin == self._pin:
            self._pin = new_pin
            return "PIN changed successfully! ✅"
        else:
            return "Incorrect old PIN! ❌"
    
    def __str__(self):
        status = "Unlocked" if not self.is_locked else "Locked"
        return f"{self.brand} {self.model} ({self.color}) - {self.storage} - Battery: {self.battery_level}% - Status: {status}"


# Inheritance - Specialized smartphone types
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, color, battery_level=100, gpu="Standard"):
        super().__init__(brand, model, storage, color, battery_level)
        self.gpu = gpu
        self._cooling_system = "Active"  # Encapsulated attribute
    
    def play_game(self, game_name):
        if self.battery_level <= 15:
            return "Battery too low for gaming! ⚡"
        if self.is_locked:
            return "Please unlock the phone first! 🔒"
        
        self.battery_level -= 15
        return f"Playing {game_name} with {self.gpu} GPU! 🎮"
    
    def boost_performance(self):
        return f"Performance boosted! {self._cooling_system} cooling system engaged. 🚀"
    
    def __str__(self):
        base_info = super().__str__()
        return f"{base_info} - GPU: {self.gpu}"


class CameraPhone(Smartphone):
    def __init__(self, brand, model, storage, color, battery_level=100, camera_mp=12):
        super().__init__(brand, model, storage, color, battery_level)
        self.camera_mp = camera_mp
        self._camera_modes = ["Photo", "Video", "Portrait", "Night"]  # Encapsulated attribute
    
    def take_photo(self):
        if self.battery_level <= 3:
            return "Battery too low to take photos! ⚡"
        if self.is_locked:
            return "Please unlock the phone first! 🔒"
        
        self.battery_level -= 3
        return f"Taken a {self.camera_mp}MP photo! 📸"
    
    def record_video(self, duration):
        if self.battery_level <= duration:
            return "Not enough battery for this video! ⚡"
        if self.is_locked:
            return "Please unlock the phone first! 🔒"
        
        self.battery_level -= duration
        return f"Recording {duration} second video with {self.camera_mp}MP camera! 🎥"
    
    def add_camera_mode(self, new_mode):
        self._camera_modes.append(new_mode)
        return f"Added {new_mode} mode to camera! ✅"
    
    def list_camera_modes(self):
        return f"Available camera modes: {', '.join(self._camera_modes)}"
    
    def __str__(self):
        base_info = super().__str__()
        return f"{base_info} - Camera: {self.camera_mp}MP"


# Polymorphism - Different phones have different special functions
class FoldablePhone(Smartphone):
    def __init__(self, brand, model, storage, color, battery_level=100):
        super().__init__(brand, model, storage, color, battery_level)
        self.is_folded = False
    
    def fold(self):
        self.is_folded = not self.is_folded
        status = "folded" if self.is_folded else "unfolded"
        return f"Phone is now {status}! 📱"
    
    def use_flex_mode(self):
        if not self.is_folded:
            return "Flex mode only works when partially folded! ⚠️"
        return "Using flex mode for enhanced multitasking! 🎛️"


class RuggedPhone(Smartphone):
    def __init__(self, brand, model, storage, color, battery_level=100, protection_rating="IP68"):
        super().__init__(brand, model, storage, color, battery_level)
        self.protection_rating = protection_rating
    
    def withstand_drop(self):
        return f"Phone survived a drop thanks to {self.protection_rating} protection! 💪"
    
    def use_torch(self):
        if self.battery_level <= 1:
            return "Battery too low for torch! ⚡"
        
        self.battery_level -= 1
        return "Torch activated! 🔦"


# Demonstration
if __name__ == "__main__":
    print("=== SMARTPHONE ECOSYSTEM ===\n")
    
    # Create different types of phones
    iphone = Smartphone("Apple", "iPhone 14", 128, "Midnight")
    gaming_phone = GamingPhone("ASUS", "ROG Phone 6", 256, "Black", gpu="Adreno 730")
    camera_phone = CameraPhone("Samsung", "Galaxy S23", 256, "Phantom Black", camera_mp=200)
    foldable_phone = FoldablePhone("Samsung", "Z Fold 4", 512, "Beige")
    rugged_phone = RuggedPhone("CAT", "S62 Pro", 128, "Black", protection_rating="IP68/MIL-STD-810H")
    
    phones = [iphone, gaming_phone, camera_phone, foldable_phone, rugged_phone]
    
    # Demonstrate basic functionality
    print("=== PHONE FUNCTIONALITY ===")
    for phone in phones:
        print(phone)
        print(phone.unlock("1234"))
        print(phone.make_call("555-1234"))
        print(phone.send_message("555-1234", "Hello!"))
        print(phone.charge(10))
        print()
    
    # Demonstrate specialized methods
    print("=== SPECIALIZED FEATURES ===")
    print(gaming_phone.play_game("Genshin Impact"))
    print(gaming_phone.boost_performance())
    print()
    
    print(camera_phone.take_photo())
    print(camera_phone.record_video(30))
    print(camera_phone.add_camera_mode("Pro"))
    print(camera_phone.list_camera_modes())
    print()
    
    print(foldable_phone.fold())
    print(foldable_phone.use_flex_mode())
    print(foldable_phone.fold())
    print()
    
    print(rugged_phone.withstand_drop())
    print(rugged_phone.use_torch())
    print()
    
    # Demonstrate encapsulation
    print("=== ENCAPSULATION DEMONSTRATION ===")
    print(f"Storage: {iphone.storage}")
    
    # Trying to change storage directly (will be prevented)
    iphone.storage = 256
    
    # Proper way to "change" pin (through internal mechanism)
    print(iphone.change_pin("1234", "5678"))
    print(iphone.unlock("5678"))
    
    # Show battery usage
    print("\n=== BATTERY USAGE ===")
    for phone in phones[:3]:  # Just first three to avoid too much output
        print(f"{phone.brand} {phone.model}: {phone.battery_level}%")