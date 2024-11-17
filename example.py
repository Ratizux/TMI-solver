from TMI import *
 
availableDishes={seafoodMisoSoup,grilledLamprey,freshTofu,riceBall,boiledTofu,stinkyTofu,secretDriedFishCrisps,dewRunnyEggs,roastedMushroom,porkBowl,friedLampreys,potatoCroquettes,porkAndTroutKebab,friedCicadaSloughs,tonkotsuRamen,tofuStew,deepFriedTofu,misoTofu,udumbaraCake,imitationBearPaw,vegetableSalad,scholarsGinkgo,porkAndMushroomStirFry,scholarsGinkgo,powerSoup,beefBowl,porkAndMushroomStirFry,nigiriSushi,creamOfMushroomSoup,shirayuki,pinkRiceBall,porkRiceBall,deepFriedShrimpTempura,pickles,okonomiyaki}
availableIngredients={seaweed,lamprey,beef,onion,pumpkin,tofu,radish,trout,pork,dew,boarMeat,venison,ibericoPork,potato,honey,cicadaSlough,chili,bambooShoot,salmon,truffle,mushroom,pufferfish,tuna,egg,shrimp,ginkgoNut,stickyRice,flour,grapes,peach,bamboo,udumbara,iceCube,butter,crab,cream,blackSalt,cucumber,octopus,sweetPotato,seaUrchin,lotusSeed,pineNut,chestnut,wagyuBeef,premiumTuna,redBean}

solver=Solver(availableDishes.difference({}),availableIngredients.difference({grapes,butter,sweetPotato}),
	economical,
	#{japanese,trendPopular,greasy,fungus,hot,legendary},{peculiar}#魔理沙
	#{japanese,homecooking,culturalHeritage,goodWithAlcohol},{economical}#华扇
	#{mild,homecooking,chinese,trendPopular,japanese,culturalHeritage},{salty,greasy}#慧音
	#{culturalHeritage,sweet,japanese,mild,premium,soup},{salty,hot}#阿求
	#{filling,homecooking,fresh},{}#森近霖之助
	#{peculiar,signature,meat,filling,trendPopular,raw},{expensive}#露米娅
	#{meat,aquatic,grilled,sweet,greasy},{peculiar,vegetarian,hot}#橙
	{economical,filling,sweet,wonderful},{}#灵梦
	#{fruity,sweet,mild,vegetarian,photogenic},{meat,homecooking}#比那名居天子
	#{legendary,sweet,dreamy,refreshing},{greasy}#因幡帝 #TODO 校验
	#{smallPortion,japanese,goodWithAlcohol,strengthBoosting,meat},{}#萃香
	)

#TODO 凉菜雕花 炸猪肉排

solutions=sorted(solver.solve())
for i in solutions[-100:]:
	i.summary()

print(len(solutions))

# TODO 红豆 炸虾天妇罗 腌黄瓜 大阪烧
# TODO 重油覆盖清淡

"""
print("菜单")
dishes=[]
for i in availableDishes:
    dishes.append(Solution(i,[],i.tags,{}))
for i in sorted(dishes):
    i.summary()
"""
