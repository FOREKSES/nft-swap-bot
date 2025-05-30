import { TonConnectUI } from '@tonconnect/ui';

document.addEventListener('DOMContentLoaded', async () => {
    const tonConnectUI = new TonConnectUI({
        manifestUrl: 'https://yourdomain.com/tonconnect-manifest.json'
    });

    const connectButton = document.getElementById('connect-wallet');
    connectButton.addEventListener('click', () => tonConnectUI.connectWallet());
    
    // Загрузка NFT пользователя
    const tgUser = Telegram.WebApp.initDataUnsafe.user;
    const nfts = await fetch(`/api/nfts?user_id=${tgUser.id}`);
    renderNFTs(nfts);
});

function renderNFTs(nfts) {
    const container = document.getElementById('nft-container');
    nfts.forEach(nft => {
        const card = document.createElement('div');
        card.className = 'nft-card';
        card.innerHTML = `
            <img src="${nft.image_url}">
            <h3>${nft.name}</h3>
            <button onclick="selectNFT('${nft.id}')">Выбрать</button>
        `;
        container.appendChild(card);
    });
}