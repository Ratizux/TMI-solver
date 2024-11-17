class Tag:
	def __init__(self,name):
		self.name=name

	def __str__(self):
		return self.name

trendPopular=Tag("流行·喜爱")
darkMatter=Tag("黑暗物质")
expensive=Tag("昂贵")
economical=Tag("实惠")
meat=Tag("肉")
aquatic=Tag("水产")
vegetarian=Tag("素")
homecooking=Tag("家常")
premium=Tag("高级")
legendary=Tag("传说")
greasy=Tag("重油")
mild=Tag("清淡")
goodWithAlcohol=Tag("下酒")
filling=Tag("饱腹")
mountainDelicacy=Tag("山珍")
seaDelicacy=Tag("海味")
western=Tag("西式")
japanese=Tag("和风")
chinese=Tag("中华")
salty=Tag("咸")
fresh=Tag("鲜")
sweet=Tag("甜")
raw=Tag("生")
signature=Tag("招牌")
photogenic=Tag("适合拍照")
refreshing=Tag("凉爽")
hot=Tag("灼热")
strengthBoosting=Tag("力量涌现")
peculiar=Tag("猎奇")
culturalHeritage=Tag("文化底蕴")
fungus=Tag("菌类")
wonderful=Tag("不可思议")
smallPortion=Tag("小巧")
dreamy=Tag("梦幻")
fruity=Tag("果味")
specialty=Tag("特产")
soup=Tag("汤羹")
grilled=Tag("烧烤")
spicy=Tag("辣")

class Ingredient:
	def __init__(self,name,cost,tags):
		self.name=str(name)
		self.cost=cost
		self.tags=set(tags)

seaweed=Ingredient("海苔",3,{fresh,vegetarian})
lamprey=Ingredient("八目鳗",14,{aquatic,signature,fresh})
beef=Ingredient("牛肉",15,{meat})
onion=Ingredient("洋葱",12,{vegetarian,fresh})
pumpkin=Ingredient("南瓜",14,{filling,vegetarian})
tofu=Ingredient("豆腐",8,{vegetarian,homecooking,mild})
radish=Ingredient("萝卜",16,{vegetarian,goodWithAlcohol})
trout=Ingredient("鳟鱼",8,{fresh,aquatic})
pork=Ingredient("猪肉",10,{meat})
dew=Ingredient("露水",10,{mild})
boarMeat=Ingredient("野猪肉",25,{meat})
venison=Ingredient("鹿肉",20,{meat})
ibericoPork=Ingredient("黑毛猪肉",35,{meat,legendary,mountainDelicacy})
potato=Ingredient("土豆",10,{vegetarian,homecooking})
honey=Ingredient("蜂蜜",15,{sweet})
cicadaSlough=Ingredient("蝉蜕",5,{peculiar})
chili=Ingredient("辣椒",2,{spicy})
bambooShoot=Ingredient("竹笋",40,{vegetarian,mild})
salmon=Ingredient("三文鱼",24,{aquatic,premium,fresh})
truffle=Ingredient("松露",50,{vegetarian,legendary,mountainDelicacy,fresh,fungus,premium})
mushroom=Ingredient("蘑菇",18,{vegetarian,fresh,fungus})
pufferfish=Ingredient("河豚",42,{aquatic,seaDelicacy,fresh})
tuna=Ingredient("金枪鱼",30,{aquatic,fresh,premium})
egg=Ingredient("鸡蛋",4,{raw})
shrimp=Ingredient("虾",30,{aquatic,fresh})
ginkgoNut=Ingredient("白果",7,{photogenic})
stickyRice=Ingredient("糯米",15,{})
flour=Ingredient("面粉",10,{filling})
grapes=Ingredient("葡萄",5,{fruity,sweet})
peach=Ingredient("桃子",10,{fruity,sweet})
bamboo=Ingredient("竹子",15,{photogenic})
udumbara=Ingredient("幻昙华",70,{legendary,dreamy,wonderful,premium})
iceCube=Ingredient("冰块",2,{refreshing})
butter=Ingredient("黄油",8,{greasy})
wagyuBeef=Ingredient("和牛",40,{meat,legendary,premium})
premiumTuna=Ingredient("极上金枪鱼",34,{aquatic,seaDelicacy,legendary,fresh,premium})
crab=Ingredient("螃蟹",10,{aquatic,premium,fresh})
cream=Ingredient("奶油",9,{homecooking,sweet,western})
blackSalt=Ingredient("黑盐",3,{salty})
cucumber=Ingredient("黄瓜",7,{homecooking,vegetarian,mild})
octopus=Ingredient("章鱼",12,{aquatic,fresh,seaDelicacy})
seaUrchin=Ingredient("海胆",18,{aquatic,premium,legendary,fresh,seaDelicacy})
sweetPotato=Ingredient("地瓜",8,{filling})
lotusSeed=Ingredient("莲子",22,{signature,mild,culturalHeritage})
pineNut=Ingredient("松子",15,{signature,mild,premium})
chestnut=Ingredient("板栗",10,{homecooking,vegetarian})
redBean=Ingredient("红豆",18,{homecooking})

class Dish:
	def __init__(self,name,price,ingredients,tags,conflicts):
		self.name=str(name)
		self.price=price
		self.ingredients=set(ingredients)
		self.tags=set(tags)
		self.conflictsTags=set(conflicts)

	def __str__(self):
		return f"「{self.name}」\n标签{[i.name for i in self.tags]}\n冲突{[i.name for i in self.conflictsTags]}"

seafoodMisoSoup=Dish("海鲜味噌汤",8,{seaweed},{economical,vegetarian,homecooking,soup},{greasy})
grilledLamprey=Dish("烤八目鳗",22,{lamprey},{aquatic,signature,grilled},{meat,vegetarian})
freshTofu=Dish("冷豆腐",21,{radish,tofu},{vegetarian,homecooking,mild,goodWithAlcohol,smallPortion},{})
riceBall=Dish("饭团",6,{seaweed},{economical,vegetarian,homecooking,filling,japanese},{})
boiledTofu=Dish("煮豆腐",22,{tofu},{vegetarian,homecooking,mild},{})
stinkyTofu=Dish("臭豆腐",24,{tofu,chili},{vegetarian,chinese,peculiar,spicy},{sweet,fruity})
secretDriedFishCrisps=Dish("秘制小鱼干",30,{trout},{aquatic,salty,fresh,smallPortion},{})
dewRunnyEggs=Dish("露水煮蛋",18,{dew,egg},{economical,mild,raw},{meat,aquatic,greasy})
roastedMushroom=Dish("烤蘑菇",18,{mushroom},{economical,vegetarian,salty,hot,fungus,grilled},{})
porkBowl=Dish("猪肉盖浇饭",20,{pork},{meat,homecooking,filling},{})
friedLampreys=Dish("炸八目鳗",27,{lamprey},{aquatic,greasy,signature},{refreshing})
potatoCroquettes=Dish("土豆可乐饼",22,{potato},{vegetarian,homecooking,greasy},{refreshing})
porkAndTroutKebab=Dish("猪肉鳟鱼熏",26,{trout,pork},{meat,aquatic,homecooking,grilled},{})
friedCicadaSloughs=Dish("香炸蝉蜕",19,{cicadaSlough},{economical,greasy,peculiar},{})
tonkotsuRamen=Dish("豚骨拉面",60,{pork,egg,seaweed},{meat,homecooking,filling,salty},{})
tofuStew=Dish("豆腐锅",19,{tofu},{economical,vegetarian,mild,japanese,hot},{})
deepFriedTofu=Dish("油豆腐",16,{tofu},{economical,vegetarian,homecooking,greasy,japanese},{})
misoTofu=Dish("豆腐味噌",21,{tofu},{vegetarian,homecooking,mild,japanese,soup},{greasy})
udumbaraCake=Dish("幻昙花糕",78,{udumbara,dew},{expensive,premium,legendary,sweet,photogenic,wonderful,dreamy},{meat,aquatic})
imitationBearPaw=Dish("赛熊掌",70,{ibericoPork,bambooShoot,pufferfish},{expensive,meat,aquatic,premium,mountainDelicacy,fresh,strengthBoosting,wonderful},{})
vegetableSalad=Dish("蔬菜专辑",56,{potato,onion,pumpkin},{vegetarian,mild,raw,refreshing},{meat,aquatic,hot})
scholarsGinkgo=Dish("诗礼银杏",60,{ginkgoNut,honey},{vegetarian,chinese,sweet,culturalHeritage},{salty})
powerSoup=Dish("力量汤",34,{seaweed,boarMeat},{meat,mountainDelicacy,hot,strengthBoosting,soup},{smallPortion,refreshing})
beefBowl=Dish("牛肉盖浇饭",20,{beef},{meat,homecooking,filling},{})
shirayuki=Dish("白雪",98,{pufferfish,lamprey,seaweed},{expensive,meat,aquatic,premium,japanese,culturalHeritage},{})
pinkRiceBall=Dish("温暖饭团",30,{onion,trout},{aquatic,vegetarian,homecooking,filling,japanese,hot},{})
porkRiceBall=Dish("炙猪肉饭团",14,{pork},{economical,meat,homecooking,filling,japanese},{})
porkAndMushroomStirFry=Dish("蘑菇肉片",20,{mushroom,pork},{meat,homecooking,greasy,fungus},{})
nigiriSushi=Dish("手握寿司",28,{salmon,tuna},{aquatic,mild,japanese,fresh,raw,culturalHeritage},{})
creamOfMushroomSoup=Dish("奶香蘑菇汤",28,{mushroom,potato,cream},{homecooking,photogenic,fungus},{})
deepFriedShrimpTempura=Dish("炸虾天妇罗",22,{shrimp,flour},{greasy,goodWithAlcohol},{mild})
pickles=Dish("腌黄瓜",16,{cucumber,blackSalt},{economical,vegetarian,goodWithAlcohol,salty,smallPortion},{})
okonomiyaki=Dish("大阪烧",24,{flour,egg,radish},{japanese,signature,photogenic,smallPortion},{})

class Solution:
	def __init__(self,dish,extraIngredients,tags,highlightedTags):
		self.dish=dish
		self.extraIngredients=extraIngredients
		self.tags=tags
		self.highlightedTags=highlightedTags
	def summary(self):
		print(f"[{self.dish.name}]")
		print(f"成本：{sum(i.cost for i in self.dish.ingredients)+sum(i.cost for i in self.extraIngredients)}，卖{self.dish.price}")
		print("食材："+",".join([i.name for i in self.dish.ingredients])+"+",end="")
		print(",".join(i.name for i in self.extraIngredients))
		print("标签："+",".join(f"<{i.name}>" if i in self.highlightedTags else i.name for i in self.tags))
	def profit(self):
		return self.dish.price-sum(i.cost for i in self.dish.ingredients)-sum(i.cost for i in self.extraIngredients)
	def __lt__(self,other):
		return self.profit()<other.profit()


class Solver:
	def __init__(self,availableDishes,availableIngredients,targetTag,preferredTags,dislikedTags):
		self.availableDishes=set(availableDishes)
		self.availableIngredients=set(availableIngredients)
		self.ingredientCount=len(self.availableIngredients)
		self.ingredientList=list(self.availableIngredients)
		self.targetTag=targetTag
		self.preferredTags=set(preferredTags)
		if targetTag in self.preferredTags:
			self.preferredTags.remove(targetTag)
		self.dislikedTags=set(dislikedTags)

	def dfs(self,dish,choice,depth,maxDepth,oldTagSet):
		if depth==maxDepth:
			return
		tagSet=oldTagSet.union(self.ingredientList[choice].tags)
		tagDifference=tagSet.difference(oldTagSet)
		if len(tagDifference)==0:
			# 剪枝，没有任何新加tag
			return
		if len(tagDifference.intersection(self.preferredTags))==0 and self.targetTag not in tagDifference:
			if len(self.ingredientList[choice].tags.intersection({meat,hot,expensive}))==0:
				# 剪枝，没有与要求标签重合，后续也没有任何无效化其他标签的可能
				return
			flag=True
			if meat in tagDifference and vegetarian in self.negativeTags:
				flag=False
			if hot in tagDifference and refreshing in self.negativeTags:
				flag=False
			if expensive in tagDifference and economical in self.negativeTags:
				flag=False
			if flag:
				return
		if meat in tagSet and vegetarian in tagSet:
			tagSet.remove(vegetarian)
		if hot in tagSet and refreshing in tagSet:
			tagSet.remove(refreshing)
		if expensive in tagSet and economical in tagSet:
			tagSet.remove(economical)
		tagDifference=tagSet.difference(oldTagSet)
		if len(tagDifference)==0:
			# 新加的tag全被覆盖了，再剪枝
			return
		if self.targetTag in tagSet and len(self.preferredTags.intersection(tagSet))>=2 and len(self.dislikedTags.intersection(tagSet))==0 and len(dish.conflictsTags.intersection(tagSet))==0:
			# 找到解了
			extraIngredients=[]
			for i in range(self.ingredientCount):
				if self.ingredientSelected[i]:
					extraIngredients.append(self.ingredientList[i])
			highlightedTags=set(self.preferredTags);
			highlightedTags.add(self.targetTag)
			self.solutions.append(Solution(dish,extraIngredients,tagSet,highlightedTags))
			return
		for i in range(choice+1,self.ingredientCount):
			self.ingredientSelected[i]=True
			self.dfs(dish,i,depth+1,maxDepth,tagSet)
			self.ingredientSelected[i]=False

	def solve(self):
		self.solutions=[]
		for i in self.availableDishes:
			if self.targetTag in i.tags and len(self.preferredTags.intersection(i.tags))>=2 and len(self.dislikedTags.intersection(i.tags))==0:
				highlightedTags=set(self.preferredTags);
				highlightedTags.add(self.targetTag)
				self.solutions.append(Solution(i,[],i.tags,highlightedTags))
				continue
			self.negativeTags=self.dislikedTags.union(i.conflictsTags)
			self.ingredientSelected=[False for i in range(self.ingredientCount)]
			for j in range(self.ingredientCount):
				self.ingredientSelected[j]=True
				self.dfs(i,j,0,5-len(i.ingredients),i.tags)
				self.ingredientSelected[j]=False
		return self.solutions



